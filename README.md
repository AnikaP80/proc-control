# Process Control Repository

This repository contains files and scripts related to process control concepts and applications. Below is a description of each file:

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Explore the scripts and notebooks to understand and simulate process control systems.
4. To run the final model, see `final_model.ipynb`.
5. To run a sample factory (static testing), see `dmcExample.py`.

## File Descriptions

- **`README.md`**: This file provides an overview of the repository and describes the purpose of each file.

- **`requirements.txt`**: A list of Python dependencies required to run the scripts and notebooks in this repository.

### Model
- **`final_model.ipynb`**: Final model to run.
    - `intermediate_model.ipynb` is between the baseline and final model. 
- **`DMC_Env.py`**: Environment for SAC model
- **`DMC_Play.py`**: "Play" for SAC model
- **`sac.py`**: Contains the code for SAC model
- **`replay_buffer.py`**: Contains the replay buffer code

### Data generation
- **`dmc.py`**: DMC_controller, which holds the "black-box" data for each DMC
- **`reward.py`**: Reward function
- **`structure.py`**: Contains the interface that the agent can speak to in order to get DMC 

### Visualization tools
- **`visualizationTools.py`**: Helpful functions for visualizing DMCs over time
- **`DMCview.md`**: auto-generated file to see the factory defined in dmcExample.py
- **`dmcExample.py`**: Please run this if you want to see the factory over time. 