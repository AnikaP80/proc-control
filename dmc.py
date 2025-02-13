import numpy as np

class DMC_controller:
    def __init__(self, functionName, goal, constraints, paramList):
        """_summary_

        Args:
            functionName (_type_): type of function the DMC uses
            goal (_type_): goal of the DMC
            paramList (_type_): list of DMC parameters/weights
        """
        self.functionName = functionName
        self.goal = goal
        self.constraints = constraints
        self.paramList = paramList
    """
    The following functions have the following general structure:
        input: inputList (e.g. T1, P1, V1)
        output: outputList (e.g. T2, P2, V2)
    """
    # 
    def _PID_controller(self, inputList):
        return inputList
    
    # 
    def _randomFunc(self, inputList):
        return inputList
    
    # wrapper to call actual update function
    # update returns output list, which typically mirrors inputList
    def update(self, inputList):
        if(self.functionName == "PID"):
            return self._PID_controller(inputList)
        elif(self.functionName == "random"):
                return self._randomFunc(inputList)
            
        return inputList
    
    
    