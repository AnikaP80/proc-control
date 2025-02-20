from structure import DMC_structure

# reminder on DMC array:
# [DMC number, list that it points to, function type, goal, constraints, parameter, DMC input]
# LAST ONE IS INPUT NOTTTT OUTPUT!!!!!
# DMC output is what iterate() returns!!!
arrLen = 3

DMCarr = [[] for i in range(arrLen + 1)]
DMCarr[0] = [0, [1], "PID", 25, [1, 0, 0], [20], [1, 1, 1]]

print("DMC array:")
for i in range(arrLen):
    DMCarr[i] = [i, [i + 1], "PID", i, [i, i, i], [i], [10, 10, 10]]

DMCarr[arrLen] = [i, [], "PID", i, [i, i, i], [i], [10, 10, 10]]
# print(DMCarr)
struct = DMC_structure(DMCarr)

print("\n\nIteration:")
for i in range(3):
    print("final output ", i, ": ", struct.iterate(), "\n")
    

# print(DMCarr)

# struct.setGoal(0, -100)

# print(DMCarr)
