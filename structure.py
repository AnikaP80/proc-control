from dmc import DMC_controller
import numpy as np
"""


    NOT DONE YET!!!


"""
class DMC_structure:
        
    def __init__(self, DMCconnectionList):
        self.DMCconnectionList = DMCconnectionList
        self.outputList = [[0, 0, 0] for _ in range(len(DMCconnectionList))]

    def setGoal(self, DMCnumber, newGoal):
        self.DMCconnectionList[DMCnumber][3] = newGoal
        # print("Set the goal of ", DMCnumber, " to ", newGoal)
        return
    
    def getGoal(self, DMCnumber):
        return self.DMCconnectionList[DMCnumber][3]
    
    def getConstraints(self, DMCnumber):
        struct = DMC_controller(self.DMCconnectionList[DMCnumber][2])
        constraints = np.array(struct.getConstraints())  # shape: (N, 2)
        outputs = np.array(self.outputList[DMCnumber])   # shape: (N,)

        full_array = np.column_stack((outputs, constraints))  # shape: (N, 3)

        fullList = full_array.tolist()
        return fullList
    
    def getSize(self):
        return len(self.outputList)
    
    """_summary_
        iterate through the DMC's and update them
        they all update at the same time, 
        and you return the updated list of DMC structure parameters
        
        
    """
    def iterate(self, newTemperatureGoals):
        num_DMCs = len(self.DMCconnectionList)
        newDMCoutputs = [[] for _ in range(num_DMCs)]
        final_output = None

        for i, (index, DMCconnections, DMCfunc, _, DMCinput) in enumerate(self.DMCconnectionList):
            struct = DMC_controller(DMCfunc)
            DMCgoal = newTemperatureGoals[i]

            # Update the current DMC
            output = struct.update(DMCgoal, DMCinput)

            # If this DMC has no outgoing connections, it's the final output
            if not DMCconnections:
                final_output = output

            # Propagate output to connected DMCs
            for adjDMC in DMCconnections:
                newDMCoutputs[adjDMC].append(output)

        # Aggregate incoming outputs and update internal state
        for i, outputs in enumerate(newDMCoutputs):
            if outputs:
                # Average element-wise over the outputs
                mean = [sum(col) / len(col) for col in zip(*outputs)]
                self.outputList[i] = mean

                # Update the last element in DMCconnectionList accordingly
                old_last = self.DMCconnectionList[i][-1]
                if old_last[2] == mean[2]:
                    self.DMCconnectionList[i][-1] = [mean[0], mean[1], float('inf')]
                else:
                    self.DMCconnectionList[i][-1] = mean

        return final_output