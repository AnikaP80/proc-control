from dmc import DMC_controller
import copy
"""


    NOT DONE YET!!!


"""
class DMC_structure:
        
    def __init__(self, DMCconnectionList):
        """_summary_  
        Args:
            DMCconnectionList: array with the following specifications:
            
            DMC Number, connected DMCs, DMC function name, goal, constraints, parameters, DMC input
            ex: 
            [[0, [1], PID, 25, [1, 0, 0], [20, ...], [25, 6, 1]],
             [1, [2], random, 10, [0, 10, 21], [10, ...], [5, 20, 100]],
             ]
             
             0 is our starting DMC
             2 is our output DMC
        """
        self.DMCconnectionList = DMCconnectionList
        self.outputList = [row[-1] for row in DMCconnectionList]

    def setGoal(self, DMCnumber, newGoal):
        self.DMCconnectionList[DMCnumber][3] = newGoal
        return
    
    def getConstraints(self, DMCnumber):
        struct = DMC_controller(self.DMCconnectionList[DMCnumber][2])
        constraints = struct.getConstraints()
        fullList = [[0, [0,0]] for _ in range(len(constraints))]
        
        for i in range(len(fullList)):
            fullList[i] = [self.outputList[DMCnumber][i], constraints[i][0], constraints[i][1]]
        return fullList
    
    
    """_summary_
        iterate through the DMC's and update them
        they all update at the same time, 
        and you return the updated list of DMC structure parameters
        
        
    """
    def iterate(self, newTemperatureGoals):
        # make copy of list
        newDMCoutputs = [[] for _ in range(len(self.DMCconnectionList))]
        newDMCoutputs[0] = self.DMCconnectionList[0][-1]
        output = []
        
        for i in range(len(self.DMCconnectionList)):
            # output = DMC(input)
            
            arr = self.DMCconnectionList[i]
            # print("arr", arr)
            DMCconnections = arr[1]
            DMCfunc=  arr[2]
            
            # GYM should update new temperature goals
            DMCgoal = arr[3]
            DMCgoal[1] = newTemperatureGoals[i] 
            
            DMCinput = arr[4]
            
            struct = DMC_controller(DMCfunc)
            output = struct.update(DMCgoal, DMCinput)
            
            # update DMCs that need the output
            # CURRENT ASSUMPTION - if two DMC's point to the same thing, 
            #   just do a basic override.
            for adjDMC in DMCconnections:
                newDMCoutputs[adjDMC] = output
        
        # update DMCconnectionList
        for i in range(len(self.DMCconnectionList)):
            self.outputList[i] = newDMCoutputs[i]
            self.DMCconnectionList[i][-1] = newDMCoutputs[i]

        return output