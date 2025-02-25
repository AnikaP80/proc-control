import numpy as np

class DMC_controller:
    def __init__(self, functionName):
        self.functionName = functionName
        self.R = 8.314
        
        # initialized later in reward function
        self.Tlow = 0
        self.Thigh = 0
        self.Plow = 0
        self.Phigh = 0
        self.Keqlow = 0
        
    def _DMC1(self, Tcurr, Tset):
        V = (np.pi) * 5 * 100
        # print("goal: ", Tset, "input: ", Tcurr)
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        Pnext = (self.R * Tnext) / V
        Keq = Tnext / 100
        return (Tnext, Pnext, Keq)
    
    def _DMC2(self, Tcurr, Tset):
        V = np.pi * 5 * 50
        # print("goal: ", Tset, "input: ", Tcurr)
        # + np.random.rand()*10 - 5
        Tcurr += 150
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        Pnext = (self.R * Tnext) / V
        Keq = Tnext / 100
        return (Tnext, Pnext, Keq)
    
    def DMC1constraints(self):
        V = np.pi * 5 * 100
        lowBound = max(0, 1.35 * V / self.R, 100 * 0.3)
        upBound = min(10000, 2.5 * V / self.R)
        # print((lowBound, upBound))
        self.Tlow = 250
        self.Thigh = 500
        self.Plow = 1.35
        self.Phigh = 2.5
        self.Keqlow = 2.8
    
    def DMC2constraints(self):
        V = np.pi * 5 * 50
        lowBound = max(0, 4.5 * V / self.R, 100 * 0.75)
        upBound = min(10000, 6 * V / self.R)
        # print((lowBound, upBound))
        
        self.Tlow = 400
        self.Thigh = 600
        self.Plow = 4.5
        self.Phigh = 6
        self.Keqlow = 4.2
    
    def update(self, goal, inputList):
        Tcurr = inputList[0]
        if self.functionName == "DMC1":
            return self._DMC1(Tcurr, goal)
        elif self.functionName == "DMC2":
            return self._DMC2(Tcurr, goal)
        return inputList
    
    def DMCreward(self, Tgoal, outputList):
        
        T = outputList[0]
        P = outputList[1]
        Keq = outputList[2]
        
        alpha = 5.0  # Weight for temperature deviation
        beta = 1.0   # Weight for pressure penalty
        gamma = 3.0  # Weight for Keq penalty
        
        # Compute temperature error
        temp_error = (T - Tgoal) ** 2 if abs(T - Tgoal) >= 5 else 0
        
        P_penalty = 0
        Keq_penalty = 0
        # Check constraints based on function type
        if self.functionName == "DMC1":
            self.DMC1constraints()
        elif self.functionName == "DMC2":
            self.DMC2constraints()
        P_penalty = 0 if self.Plow <= P <= self.Phigh else max(P - self.Phigh, self.Plow-P)
        Keq_penalty = 0 if Keq >= 0.3 else (0.3 - Keq)  # Constraint from archived functions
        # Reward function
        reward = -alpha * temp_error - beta * P_penalty - gamma * Keq_penalty + 1
        return reward
