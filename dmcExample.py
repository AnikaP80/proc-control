from visualizationTools import simVis, displayDMCWebMermaid

# This is an example of a DMC (Dynamic Matrix Control) system.
# It is a simplified version of a chemical process control system, with static inputs.
# The DMC system consists of several units, each with its own temperature, pressure, and equilibrium constant.
# This is set that the goal is at the max Keq for each unit.

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

# Get the graphs
simVis(DMCarr)

# Generate the mermaid code for the DMC system
displayDMCWebMermaid(DMCarr)