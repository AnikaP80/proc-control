from structure import DMC_structure
from reward import reward_function
import matplotlib.pyplot as plt
import math 

def simVis(arr):
    print("DMC array:", arr)
    struct = DMC_structure(arr)

    print("\n\nIteration:")
    n_iter = 100
    n_dmcs = len(arr)

    # Initialize storage
    all_constraints = [[] for _ in range(n_dmcs)]
    all_goals = [[] for _ in range(n_dmcs)]
    all_rewards = []
    final_outputs = []

    # Iterate
    for x in range(n_iter):
        tempGoals = [dmc[3] for dmc in arr]
        if x >= 50 and x <= 75:
            tempGoals[1] = 10
            # print("updated temp")
        # print(tempGoals)
        final_output = struct.iterate(tempGoals)
        # print(reward_function(struct, final_output))
        all_rewards.append(reward_function(struct, final_output))
        final_outputs.append(final_output)

        for i in range(n_dmcs):
            goal = struct.getGoal(i)
            constraints = struct.getConstraints(i)

            if constraints:
                # Only store if there's output
                all_constraints[i].append([row[0] for row in constraints])  # just T for now
            else:
                all_constraints[i].append(None)

            all_goals[i].append(goal)
        # print(all_goals)

    # Plotting
    iterations = list(range(1, n_iter + 1))

    cols = 4  # number of plots per row
    rows = math.ceil((n_dmcs + 1) / cols)
    fig, axs = plt.subplots(rows, cols, figsize=(cols * 6, rows * 4), sharex=True)

    axs = axs.flatten()
        
    for i in range(n_dmcs):
        base_ax = axs[i]

        # Extract each metric over time (skip None)
        T_vals = [c[0] if c else None for c in all_constraints[i]]
        P_vals = [c[1] if c else None for c in all_constraints[i]]
        K_vals = [c[2] if c else None for c in all_constraints[i]]

        goal_T = [g if g else None for g in all_goals[i]]

        # Temperature (left y-axis)
        base_ax.plot(iterations, T_vals, label="T", color="tab:red")
        base_ax.plot(iterations, goal_T, '--', label="T goal", color="tab:red")
        base_ax.set_ylabel("Temp (°C)", color="tab:red")
        base_ax.tick_params(axis='y', labelcolor="tab:red")

        # Pressure (right y-axis)
        ax2 = base_ax.twinx()
        ax2.plot(iterations, P_vals, label="P", color="tab:blue")
        ax2.set_ylabel("Pressure", color="tab:blue")
        ax2.tick_params(axis='y', labelcolor="tab:blue")

        # Keq (right y-axis, offset)
        ax3 = ax2.twinx()
        ax3.spines["right"].set_position(("outward", 60))  # offset the third axis
        ax3.plot(iterations, K_vals, label="Keq", color="tab:green")
        ax3.set_ylabel("Keq", color="tab:green")
        ax3.tick_params(axis='y', labelcolor="tab:green")

        # Title and shared x-axis
        base_ax.set_title(f"DMC{i}: {arr[i][2]}")
        base_ax.set_xlabel("Iteration")

    ax = axs[n_dmcs]
    ax.plot(iterations, all_rewards, label="Reward")
    ax.set_title("Reward func")
    ax.set_xlabel("Iteration")
    
    # Hide unused axes
    for j in range(n_dmcs + 1, len(axs)):
        fig.delaxes(axs[j])

    fig.suptitle("Outputs and Goals Per DMC Over Time", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    
def displayDMCWebMermaid(arr):
    lines = ["```mermaid", "flowchart TD"]
    for node in arr:
        index, next_nodes, func, *_ = node
        label = f'{index}["{func}"]'
        if next_nodes:
            for target in next_nodes:
                if target != index:
                    lines.append(f"  {label} --> {target}")
        else:
            lines.append(f"  {label} --> out")
    
    lines.append("subgraph inputs")
    for node in arr:
        index, next_nodes, func, *_ = node
        label = f'   {index}:::inStyle'
        if next_nodes and (index in next_nodes):
            lines.append(label)
    lines.append("end")
    
    lines.append("subgraph internals")
    for node in arr:
        index, next_nodes, func, *_ = node
        label = f'{index}'
        lines.append(f"  {label}")
    lines.append("end")
    lines.append("classDef inStyle fill:#bbf")
    lines.append("text[\"inputs have implicit self-loop\"]")
    lines.append("```")
    with open("DMCview.md", "w") as f:
        f.write("\n".join(lines))