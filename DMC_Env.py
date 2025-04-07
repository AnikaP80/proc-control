import gym
from gym import spaces
import numpy as np
from structure import DMC_structure

class DMC_Env(gym.Env):
    """
    Custom Environment following the OpenAI Gym interface.
    
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, DMCarr):
        super(DMC_Env, self).__init__()
        
        #TODO no way this is right - Create the structure from DMCarr
        self.struct = DMC_structure(DMCarr)
        
        # Determine the number of DMCs, which is also the dimensionality of the action space.
        num_DMC = len(DMCarr)
        
  # --- Define ACTION SPACE ---
        # For the action space, we use only the temperature constraints from each DMC.
        action_low = []
        action_high = []
        for i in range(num_DMC):
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
        obs_low = []
        obs_high = []
        for i in range(num_DMC):
            constraints = self.struct.getConstraints(i)
            for param in constraints:
                # Each param is a triplet: [actual, lower_bound, upper_bound]
                obs_low.append(param[1])
                obs_high.append(param[2])
        self.observation_space = spaces.Box(low=np.array(obs_low, dtype=np.float32),
                                            high=np.array(obs_high, dtype=np.float32),
                                            dtype=np.float32)
        
        # --- Initialize State ---
        # For the initial state, we use the "actual" value of each parameter for every DMC.
        state = []
        for i in range(num_DMC):
            constraints = self.struct.getConstraints(i)
            for param in constraints:
                state.append(param[0])
        self.state = np.array(state, dtype=np.float32)
        
        self.steps = 0
        self.max_steps = 200

    def reset(self):
        """
        TODO: Resets the environment to an initial state and returns the initial observation.
        """
        # Start at position 0 with zero velocity.
        self.state = np.array([0.0, 0.0], dtype=np.float32)
        self.steps = 0
        return self.state

    def step(self, action):
        """
        TODO: Executes one time step in the environment given an action.
        
        Parameters:
            action (np.ndarray): An array containing the force to apply.
            
        Returns:
            state (np.ndarray): The new state after applying the action.
            reward (float): The reward achieved in this step.
            done (bool): Whether the episode has ended.
            info (dict): Additional diagnostic information (empty in this case).
        """
        # Ensure the action is within the allowed range.
        action = np.clip(action, self.action_space.low, self.action_space.high)
        
        pos, vel = self.state
        
        # Update dynamics: new velocity and new position.
        new_vel = vel + action[0] * self.dt
        new_pos = pos + new_vel * self.dt
        
        self.state = np.array([new_pos, new_vel], dtype=np.float32)
        self.steps += 1
        
        # Compute the reward as the negative distance from the target.
        reward = -abs(new_pos - self.target)
        
        # Determine if the episode is done.
        done = False
        # Episode is done if the position is close enough to the target.
        if abs(new_pos - self.target) < 0.1:
            done = True
        # Or if the maximum number of steps is reached.
        if self.steps >= self.max_steps:
            done = True
        
        info = {}
        return self.state, reward, done, info

    def render(self, mode='human'):
        """
        TODO: Renders the current state of the environment.
        For simplicity, this implementation prints the state to the console.
        """
        pos, vel = self.state
        print(f"Step: {self.steps}, Position: {pos:.2f}, Velocity: {vel:.2f}")

    def close(self):
        """
        Performs any necessary cleanup.
        """
        pass
