import argparse
import logging
import os
import numpy as np
from sac import Actor
from DMC_Env import DMC_Env  # Import your custom environment

logging.basicConfig(level='INFO')

def main(cli_args=None):
    """
    Run a single episode of the trained SAC policy on the DMC environment.
    Loads weights from HDF5 (.h5) format.
    Ensures model variables are built before loading.
    """
    parser = argparse.ArgumentParser(description='DMC Play')
    parser.add_argument('--seed',       type=int, default=42, help='random seed')
    parser.add_argument('--render',     action='store_true', help='render environment')
    parser.add_argument('--verbose',    action='store_true', help='log execution details')
    parser.add_argument('--model_root', type=str, default='./data/models/',
                        help='parent directory for saved models')
    parser.add_argument('--model_name', type=str, required=True,
                        help='timestamp folder name of saved model')
    args = parser.parse_args(cli_args)

    # Determine the model directory
    model_root = os.path.normpath(args.model_root)
    model_dir = os.path.join(model_root, args.model_name)
    if args.verbose:
        logging.info(f"Loading weights from directory: {model_dir}")
        logging.info(f"Directory contents: {os.listdir(model_dir)}")

    # Build environment
    DMCarr = [[] for _ in range(10)]
    DMCarr[0] = [0, [0, 1], "DMC0", 400, [350, 5, 1]]
    DMCarr[1] = [1, [2],    "DMC1", 400, [350, 5, 1]]
    DMCarr[2] = [2, [3, 5], "DMC2", 450, [350, 5, 1]]
    DMCarr[3] = [3, [4],    "DMC3", 420, [350, 5, 1]]
    DMCarr[4] = [4, [5],    "DMC4", 500, [450, 5, 1]]
    DMCarr[5] = [5, [],     "DMC5", 350, [350, 5, 1]]
    DMCarr[6] = [6, [1, 6], "DMC6", 350, [350, 5, 1]]
    DMCarr[7] = [7, [3, 7], "DMC7", 470, [350, 5, 1]]
    DMCarr[8] = [8, [5, 8], "DMC8", 400, [350, 5, 1]]
    DMCarr[9] = [9, [2, 3, 4, 9], "DMC9", 500, [350, 5, 1]]

    env = DMC_Env(DMCarr)

    # Rebuild and load the policy network
    actor = Actor(env.action_space.shape[0])

    # Build variables by a dummy forward pass before loading HDF5 weights
    dummy_state = np.zeros((1, env.observation_space.shape[0]), dtype=np.float32)
    _ = actor(dummy_state)

    # Load from HDF5
    h5_path = os.path.join(model_dir, 'policy.h5')
    if os.path.isfile(h5_path):
        actor.load_weights(h5_path)
        if args.verbose:
            logging.info(f"Loaded weights from HDF5 file: {h5_path}")
    else:
        raise FileNotFoundError(f"HDF5 file not found at {h5_path}")

    # Run one episode and print actions
    state = env.reset()
    done = False
    episode_reward = 0.0
    last_action = None

    while not done:
        if args.render:
            env.render()
        state_input = np.array(state, ndmin=2)
        action_tensor, _ = actor(state_input)
        action = action_tensor.numpy()[0]
        last_action = action
        print("Action:", action)
        state, reward, done, _ = env.step(action)
        episode_reward += reward

    print(f"Episode reward: {episode_reward}")
    print("Last Action", last_action)

if __name__ == '__main__':
    main()
