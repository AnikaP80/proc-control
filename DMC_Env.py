import gym
from gym import spaces
import numpy as np
from structure import DMC_structure
from reward import reward_function

class DMC_Env(gym.Env):
    """
    Custom Environment following the OpenAI Gym interface.
    
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, DMCarr):
        super(DMC_Env, self).__init__()
        
        # Create DMC_structure
        self.struct = DMC_structure(DMCarr)
        
        # Determine the number of DMCs, which is also the dimensionality of the action space.
        self.num_DMC = len(DMCarr)

        # Instead of using the large real-range as the Gym action_space,
        # define it as [-1, +1] for each dimension:
        self.action_space = spaces.Box(
            low  = -1.0,
            high =  1.0,
            shape=(self.num_DMC,),
            dtype=np.float32
        )

        # But we still need to remember the true real range for each DMC:
        # e.g. for DMC i, the "real" action range is [low_i, high_i].
        # Suppose you already know them or build them with constraints:
        real_action_lows = []
        real_action_highs = []
        for i in range(self.num_DMC):
            constraints = self.struct.getConstraints(i)
            # The first row in each constraints array is your "temperature" item.
            # constraints[0][1] is the min, constraints[0][2] is the max
            real_action_lows.append(constraints[0][1])
            real_action_highs.append(constraints[0][2])

        self.real_action_low = np.array(real_action_lows, dtype=np.float32)
        self.real_action_high = np.array(real_action_highs, dtype=np.float32)

        # For the observation space, your existing approach is OK,
        # or you can keep it simpler. We'll just keep your style:
        obs_dim = 3 * self.num_DMC  # if each DMC has 3 parameters
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(obs_dim,), dtype=np.float32
        )

        # Initialize
        self.resetState = self._init_state()
        self.state = self.resetState.copy()
        self.steps = 0
        self.max_steps = 200

    def _init_state(self):
        state_vals = []
        for i in range(self.num_DMC):
            constraints = self.struct.getConstraints(i)
            for param in constraints:
                state_vals.append(param[0])
        return np.array(state_vals, dtype=np.float32)

    def reset(self):
        self.state = self.resetState.copy()
        self.steps = 0
        return self.state

    def step(self, raw_action):
        # 1) The agent’s action is in [-1, +1]. Scale it to the real domain:
        scaled_action = self._scale_action(raw_action)
        # print("raw action", raw_action)
        # print("scaled action", scaled_action)

        # 3) Step the environment:
        output = self.struct.iterate(scaled_action)

        # Rebuild self.state from constraints
        tempstate = []
        for i in range(self.num_DMC):
            constraints = self.struct.getConstraints(i)
            for param in constraints:
                tempstate.append(param[0])
        self.state = np.array(tempstate, dtype=np.float32)
        self.steps += 1

        # print(output)

        # Reward
        rew = reward_function(self.struct, output)

        # Done?
        done = (self.steps >= self.max_steps)
        info = {}

        return self.state, rew, done, info

    def _scale_action(self, raw_action):
        """
        Convert an action in [-1,+1] to [low,high].
        """
        # Transform each component:  scaled = low + 0.5*(raw+1)*(high - low)
        # shape = (num_DMC,)
        return self.real_action_low + 0.5*(raw_action + 1.0)*(
            self.real_action_high - self.real_action_low
        )

    def close(self):
        pass

