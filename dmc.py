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
        # paramlist = alpha, beta, gamma, delta, labmd, Tset, P, T, Keq
        self._paramInit_(paramList)
        self._phiInit_(self.alpha, self.beta, self.gamma, self.delta, self.lambd, self.Tset, self.P, self.T, self.Keq)
        
    """
    The following functions have the following general structure:
        input: inputList (e.g. T1, P1, V1)
        output: outputList (e.g. T2, P2, V2)
    """
    # 
    def _DMC1(self, phi1, phi2, phi3, Tcurr, R, V):
        Tnext = phi1*Tcurr + phi2*Tcurr + phi3
        Pnext = (R*Tnext)/V
        Keq = 283.971 + 13323/(Tnext + 50)
        return (Tnext, Pnext, Keq)
    
    # 
    def _DMC2(self, phi1, phi2, phi3, Tcurr, R, V):
        Tnext = 3*phi1*Tcurr + phi2*Tcurr/2 + phi3
        Pnext = (R*Tnext)/V
        Keq = 283.971 + 13323/(Tnext + 50)
        return (Tnext, Pnext, Keq)
    
    # alpha, beta, gamma, delta, lambda are lists
    def _phiInit_(self, alpha, beta, gamma, delta, lambd, Tset, P, T, Keq):
        self.phi1 = (alpha[0]*Tset + beta[0]*P + gamma[0]*Keq + delta[0])/(lambd[0] + np.abs(T - Tset))
        self.phi2 = (alpha[1]*Tset + beta[1]*P*P + gamma[1]*Keq + delta[1])/(lambd[1] + np.sqrt(np.abs(T-Tset)))
        self.phi3 = (alpha[2]*Tset + beta[2]*np.log(P+1) + gamma[2]*Keq + delta[2])/(lambd[2]+np.exp(-1*np.abs(T-Tset)))
    
    def _paramInit_(self, paramList):
        self.alpha = paramList[0]
        self.beta = paramList[1]
        self.gamma = paramList[2]
        self.delta = paramList[3]
        self.lambd = paramList[4]
        self.Tset = paramList[5]
        self.P = paramList[6]
        self.Tprev = paramList[7]
        self.Keq = paramList[8]
        
    # wrapper to call actual update function
    # update returns output list, which typically mirrors inputList
    def update(self, inputList):
        if(self.functionName == "PID"):
            return self._PID_controller(inputList)
        elif(self.functionName == "random"):
                return self._randomFunc(inputList)
            
        return inputList
    
    
    