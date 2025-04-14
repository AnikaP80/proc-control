from dmc import DMC_controller
import numpy as np
"""


    NOT DONE YET!!!


"""
class DMC_structure:
        
    def __init__(self, DMCconnectionList):
        self.DMCconnectionList = DMCconnectionList
        self.outputList = [row[-1] for row in DMCconnectionList]

    def setGoal(self, DMCnumber, newGoal):
        self.DMCconnectionList[DMCnumber][3] = newGoal
        # print("Set the goal of ", DMCnumber, " to ", newGoal)
        return
    
    def getGoal(self, DMCnumber):
        return self.DMCconnectionList[DMCnumber][3]
    
    def getConstraints(self, DMCnumber):
        struct = DMC_controller(self.DMCconnectionList[DMCnumber][2])
        constraints = struct.getConstraints()
        fullList = [[0, [0,0]] for _ in range(len(constraints))]
        
        for i in range(len(fullList)):
            fullList[i] = [self.outputList[DMCnumber][i], constraints[i][0], constraints[i][1]]
        return fullList
    
    def getSize(self):
        return len(self.outputList)
    
    """_summary_
        iterate through the DMC's and update them
        they all update at the same time, 
        and you return the updated list of DMC structure parameters
        
        
    """
    def iterate(self, newTemperatureGoals):
        # make copy of list
        newDMCoutputs = [[] for _ in range(len(self.DMCconnectionList))]
        output = []
        
        for i in range(len(self.DMCconnectionList)):
            arr = self.DMCconnectionList[i]
            
            # print("arr", arr)
            DMCconnections = arr[1]
            DMCfunc=  arr[2]
            
            # GYM should update new temperature goals
            DMCgoal = newTemperatureGoals[i] 
            
            DMCinput = arr[4]
            
            struct = DMC_controller(DMCfunc)
            if DMCconnections == []:
                finaloutput = struct.update(DMCgoal, DMCinput)
            output = struct.update(DMCgoal, DMCinput)
            
            # update DMCs that need the output
            for adjDMC in DMCconnections:
                newDMCoutputs[adjDMC].append(output)
        
        
        # update DMCconnectionList
        for i in range(len(self.DMCconnectionList)):
            self.outputList[i] = [sum(col) / len(col) for col in zip(*newDMCoutputs[i])]
            # print(self.outputList[i])
            self.DMCconnectionList[i][-1] = [sum(col) / len(col) for col in zip(*newDMCoutputs[i])]

        return finaloutput