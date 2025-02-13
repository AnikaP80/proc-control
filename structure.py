from dmc import DMC_controller

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

    
    """_summary_
        iterate through the DMC's and update them
        they all update at the same time, 
        and you return the updated list of DMC structure parameters
        
        
    """
    def iterate(self):
        # make copy of list
        newDMCconnectionList = self.DMCconnectionList
        output = []
        for i in range(len(self.DMCconnectionList)):
            # output = DMC(input)
            arr = self.DMCconnectionList[i]
            DMCparams = arr[2:6]
            DMCinput = arr[6]
            output = DMC_controller(*(DMCparams)).update(DMCinput)
            
            # update DMCs that need the output
            # CURRENT ASSUMPTION - if two DMC's point to the same thing, 
            #   just do a basic override.
            
            connectedDMCs = arr[1]
            for adjDMC in connectedDMCs:
                newDMCconnectionList[adjDMC][-1] = output
            print("DMC", i, "'s output: ", output)
        
        # update DMCconnectionList
        self.DMCconnectionList = newDMCconnectionList
        return output