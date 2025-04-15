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
    DMCarr = [[] for i in range(10)]
            # index, next, func, goal, input (T, P, Keq)
    DMCarr[0] = [0, [0, 1], "DMC0", 400, [350, 5, 1]]
    DMCarr[1] = [1, [2], "DMC1", 400, [350, 5, 1]]
    DMCarr[2] = [2, [3, 5], "DMC2", 450, [350, 5, 1]]
    DMCarr[3] = [3, [4], "DMC3", 420, [350, 5, 1]]
    DMCarr[4] = [4, [5], "DMC4", 500, [450, 5, 1]]
    DMCarr[5] = [5, [], "DMC5", 350, [350, 5, 1]]
    DMCarr[6] = [6, [1, 6], "DMC6", 350, [350, 5, 1]]
    DMCarr[7] = [7, [3, 7], "DMC7", 470, [350, 5, 1]]
    DMCarr[8] = [8, [5, 8], "DMC8", 400, [350, 5, 1]]
    DMCarr[9] = [9, [2, 3, 4, 9], "DMC9", 500, [350, 5, 1]]
    print("DMC array:", DMCarr)

    # Instantiate the custom environment with DMCarr.
    env = DMC_Env(DMCarr)

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
