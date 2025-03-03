from structure import DMC_structure
from dmc import DMC_controller
# reminder on DMC array:
# LAST ONE IS INPUT NOTTTT OUTPUT!!!!!
# DMC output is what iterate() returns!!!
import matplotlib.pyplot as plt

example_DMCarr = [[] for i in [0, 1]]
            # index, next, func, goal, input (T, P, Keq)
example_DMCarr[0] = [0, [0, 1], "DMC1", 400, [350, 5, 1]]
example_DMCarr[1] = [1, [], "DMC2", 500, [350, 5, 1]]

print("DMC array:", example_DMCarr)
example_struct = DMC_structure(example_DMCarr)

print("\n\nIteration:")
example_o1 = [[] for i in range(100)]
example_o2 = [[] for i in range(100)]
example_goals1 = [[] for i in range(100)]
example_goals2 = [[] for i in range(100)]

for i in range(99):
    if i == 50:
        example_DMCarr[0][-1] = [200, 5, 1]
    if i == 75:
        example_DMCarr[0][-2] = 200
        example_DMCarr[1][-2] = 400
    example_o2[i] = example_struct.iterate()
    example_o1[i] = example_DMCarr[1][-1]
    
    example_goals1[i] = example_DMCarr[0][3]
    example_goals2[i] = example_DMCarr[1][3]
    # print(o2[i])
    # print(f"Final output {i}: {[round(val, 2) for val in outputs]}\n\n")

print("constraints")
print(example_struct.getConstraints(0))
# Extract a specific metric (e.g., temperature)
example_t1 = [output[0] for output in example_o1 if output]  # Extracting T values
example_t2 = [output[0] for output in example_o2 if output]  # Extracting T
example_h1 = [goal for goal in example_goals1 if goal]
example_h2 = [goal for goal in example_goals2 if goal]
example_iterations = list(range(1, len(example_t1) + 1))

plt.plot(example_iterations, example_t1, label="t1", marker='o')
plt.plot(example_iterations, example_t2, label="t2", marker='s')
plt.plot(example_iterations, example_h1, label="g1", marker='o')
plt.plot(example_iterations, example_h2, label="g2", marker='s')

plt.xlabel("Iteration")
plt.ylabel("Values")
plt.title("DMC Outputs Over Iterations")
plt.legend()
plt.show()

# n_reward = 0

#for each DMC
# for i in range(len(DMCarr)):
#     #get all constraints of the DMC
#     for bound in struct.getConstraints(i):
#         #bound: [current, LB, UB]
#         buffer = (bound[2]-bound[1])*0.1
#         #if inf bounds, just have zero buffer - TODO: make this better
#         if buffer == float('inf'):
#             buffer = 0
#         print("buffer is", buffer,"lower bound is", bound[1], "upper bound is", bound[2])
#         UBB = bound[2] - buffer
#         LBB = bound[1] + buffer
#         print(bound[0], LBB, UBB)
#         if bound[0] > LBB and bound[0] < UBB:
#             nwd = 0
#         else:
#             #TODO: make a more sophisticated negative reward, i.e. exponential curve
#             nwd = 5

#         n_reward += nwd

# print("negative reward", n_reward)

    

