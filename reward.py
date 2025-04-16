import numpy as np

def reward_function(struct, output):
    """
    Improved reward function for RL agent controlling DMCs.
    Balances production (Keq), safety (constraint violations), and stability.
    """
    keq = float(output[2])
    reward = 100.0 * keq  # Production-focused reward
    # print(output)
    penalty = 0.0

    for i in range(struct.getSize()):
        constraints = np.array(struct.getConstraints(i))  # shape: (N, 3)
        if constraints.size == 0:
            continue  # skip empty constraints
        
        values = constraints[:, 0]
        lbs = constraints[:, 1]
        ubs = constraints[:, 2]

        # Handle infinite upper bounds
        range_spans = np.where(ubs < np.inf, ubs - lbs, 1.0)
        centers = np.where(ubs < np.inf, (ubs + lbs) / 2, lbs * 2)

        norm_offsets = np.abs(values - centers) / range_spans
        penalty += np.sum(norm_offsets**2)

        # Hard penalties
        out_of_bounds = (values < lbs) | (values > ubs)
        penalty += np.sum(out_of_bounds) * 5.0

        # Reward in-bounds
        in_bounds = ~out_of_bounds
        penalty -= np.sum(in_bounds) * 2.0
    
    reward -= penalty

    reward = reward * 0.02 #this is to keep reward roughly between 1 and 10 for training.
    # print(reward)
    return reward