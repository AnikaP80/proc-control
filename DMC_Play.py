import argparse
import logging
from datetime import datetime
import numpy as np

# Import your SAC Actor and the custom environment
from sac import Actor
from DMC_Env import DMC_Env  # Import your custom environment

# from https://github.com/shakti365/soft-actor-critic/blob/master/src/play.py

logging.basicConfig(level='INFO')

parser = argparse.ArgumentParser(description='SAC')
parser.add_argument('--seed', type=int, default=42, help='random seed')
parser.add_argument('--render', type=bool, default=False, help='set gym environment to render display')
parser.add_argument('--verbose', type=bool, default=False, help='log execution details')
parser.add_argument('--model_path', type=str, default='../data/models/', help='path to save model')
parser.add_argument('--model_name', type=str,
                    default=f'{str(datetime.utcnow().date())}-{str(datetime.utcnow().time())}',
                    help='name of the saved model')

while True:
    args = parser.parse_args()

    # Define your DMC connection list (DMCarr) as needed by your DMC_Env.
    DMCarr = [[] for _ in range(2)]
    # Each entry: [DMC Number, connected DMCs, function name, goal, DMC input (e.g., [temp, pressure, Keq])]
    DMCarr[0] = [0, [1], "DMC1", 400, [350, 5, 1]]  # DMC 0
    DMCarr[1] = [1, [], "DMC2", 500, [360, 4, 2]]      # DMC 1
    print("DMC array:", DMCarr)

    # Instantiate the custom environment with DMCarr.
    env = DMC_Env(DMCarr)
    env.seed(args.seed)

    # Get the dimensions from the environment's spaces.
    state_space = env.observation_space.shape[0]
    action_space = env.action_space.shape[0]

    # Instantiate the Actor with the number of actions (dimensions).
    actor = Actor(action_space)
    actor.load_weights(args.model_path + args.model_name + '/model')

    # Reset the environment to get the initial state.
    current_state = env.reset()
    episode_reward = 0
    done = False

    while not done:
        if args.render:
            env.render()

        # Reshape the state to match the Actor's expected input shape.
        current_state_ = np.array(current_state, ndmin=2)
        action_, _ = actor(current_state_)
        action = action_.numpy()[0]

        # Step through the environment using the action.
        next_state, reward, done, _ = env.step(action)
        episode_reward += reward

        # Update current state.
        current_state = next_state

    print("Episode reward:", episode_reward)
