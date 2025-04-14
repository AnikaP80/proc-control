def reward_function(struct, output):
    """
    Improved reward function for RL agent controlling DMCs.
    Balances production (Keq), safety (constraint violations), and stability.
    """
    keq = float(output[2])
    reward = 10.0 * keq  # Production-focused reward

    penalty = 0.0

    for i in range(len(struct.getSize())):
        for bound in struct.getConstraints(i):  # [current, LB, UB]
            value, lb, ub = bound
            range_span = ub - lb if ub < float('inf') else 1.0  # avoid inf issues

            # Soft penalty as value nears the bounds
            center = (ub + lb) / 2
            norm_offset = abs(value - center) / (range_span / 2)
            penalty += norm_offset**2  # quadratic penalty increases fast near edges

            # Hard penalty if out of bounds
            if value < lb or value > ub:
                penalty += 5.0

    reward -= penalty
    return reward