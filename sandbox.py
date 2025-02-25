from structure import DMC_structure
from dmc import DMC_controller
# reminder on DMC array:
# LAST ONE IS INPUT NOTTTT OUTPUT!!!!!
# DMC output is what iterate() returns!!!

DMCarr = [[] for i in [0, 1, 2]]
            # index, next, fung, goal, input (T, P, Keq)
DMCarr[0] = [0, [0, 1], "DMC1", 400, [350, 5, 1]]
DMCarr[1] = [1, [2], "DMC2", 500, [350, 5, 1]]
DMCarr[2] = [2, [], "Dummy", 0, [0, 0, 0]]

print("DMC array:", DMCarr)
struct = DMC_structure(DMCarr)

print("\n\nIteration:")
o1 = [[] for i in range(100)]
o2 = [[] for i in range(100)]
goals1 = [[] for i in range(100)]
goals2 = [[] for i in range(100)]

for i in range(99):
    if i == 50:
        DMCarr[0][-1] = [350, 5, 1]
    struct.iterate()
    o1[i] = DMCarr[1][-1]
    # print(o1[i])
    o2[i] = DMCarr[2][-1]
    goals1[i] = DMCarr[0][3]
    goals2[i] = DMCarr[1][3]
    # print(o2[i])
    # print(f"Final output {i}: {[round(val, 2) for val in outputs]}\n\n")


import matplotlib.pyplot as plt
# print(o1)
# print(o2)
# Extract a specific metric (e.g., temperature)
t1 = [output[0] for output in o1 if output]  # Extracting T values
t2 = [output[0] for output in o2 if output]  # Extracting T
h1 = [goal for goal in goals1 if goal]
h2 = [goal for goal in goals2 if goal]
iterations = list(range(1, len(t1) + 1))

plt.plot(iterations, t1, label="t1", marker='o')
plt.plot(iterations, t2, label="t2", marker='s')
plt.plot(iterations, h1, label="g1", marker='o')
plt.plot(iterations, h2, label="g2", marker='s')

plt.xlabel("Iteration")
plt.ylabel("Values")
plt.title("DMC Outputs Over Iterations")
plt.legend()
plt.show()