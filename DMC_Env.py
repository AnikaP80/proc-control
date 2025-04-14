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
        
        # --- Define ACTION SPACE ---
        # For the action space, we use only the temperature constraints from each DMC.
        # Range of temperature inputs - the low, high "these are valid" = constraint
        action_low = []
        action_high = []
        for i in range(self.num_DMC):
            constraints = self.struct.getConstraints(i)
            
            # We assume the first triplet corresponds to temperature: [actual, lower_bound, upper_bound]
            temp_constraint = constraints[0]
            action_low.append(temp_constraint[1])
            action_high.append(temp_constraint[2])
        self.action_space = spaces.Box(low=np.array(action_low, dtype=np.float32),
                                       high=np.array(action_high, dtype=np.float32),
                                       dtype=np.float32)
        
        # --- Define OBSERVATION SPACE ---
        # For the observation space, include the lower and upper bounds for every parameter of every DMC.
        # get the triplet of constraints per DMC ** make -inf to inf
        obs_low = []
        obs_high = []
        for i in range(self.num_DMC):
            for param in constraints:
                # Each param is a triplet: [actual, lower_bound, upper_bound]
                obs_low.append(-1*float('inf'))
                obs_high.append(float('inf'))
        self.observation_space = spaces.Box(low=np.array(obs_low, dtype=np.float32),
                                            high=np.array(obs_high, dtype=np.float32),
                                            dtype=np.float32)
        
        # --- Initialize State ---
        # For the initial state, we use the "actual" value of each parameter for every DMC.
        state = []
        for i in range(self.num_DMC):
            constraints = self.struct.getConstraints(i)
            for param in constraints:
                state.append(param[0])
        self.state = np.array(state, dtype=np.float32)
        self.resetState = np.array(state, dtype=np.float32)
        self.steps = 0
        self.max_steps = 200

    def reset(self):
        """
        TODO: Resets the environment to an initial state and returns the initial observation.
        """
        # Start at position 0 with zero velocity.
        self.state = np.array(self.resetState, dtype=np.float32)
        self.steps = 0
        return self.state

    def step(self, action):
        """
        Anika note: very similar to iterate
        TODO: Executes one time step in the environment given an action.
        
        Parameters:
            action (np.ndarray): An array containing the new temperature goal of each DMC.
            
        Returns:
            state (np.ndarray): The new state after applying the action.
            reward (float): The reward achieved in this step.
            done (bool): Whether the episode has ended.
            info (dict): Additional diagnostic information (empty in this case).
        """
        # Ensure each action is within the allowed range.
        for temp in action:
            temp = np.clip(temp, self.action_space.low, self.action_space.high)
        
        
        # Update dynamics: new velocity and new position.
        # print(action)
        output = self.struct.iterate(action)
        
        tempstate = []
        for i in range(self.num_DMC):
            constraints = self.struct.getConstraints(i)
            for param in constraints:
                tempstate.append(param[0])
        self.state = np.array(tempstate, dtype=np.float32)
        self.steps += 1
        
        # PUT ACTUAL REWARD FUNCTION HERE
        rew = reward_function(self.struct, output)
        
        # Determine if the episode is done.
        done = False
        if self.steps >= self.max_steps:
            done = True
        
        info = {}
        return self.state, rew, done, info

    # def render(self, mode='human'):
    #     """
    #     TODO: Renders the current state of the environment.
    #     For simplicity, this implementation prints the state to the console.
    #     """
    #     pos, vel = self.state
    #     print(f"Step: {self.steps}, Position: {pos:.2f}, Velocity: {vel:.2f}")

    def close(self):
        """
        Performs any necessary cleanup.
        """
        pass
