import numpy as np

class DMC_controller:
    def __init__(self, functionName):
        self.functionName = functionName
        self.R = 8.314
        
    def _DMC0(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = (np.pi) * 5 * 100
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        Keq = Tnext / 100 
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC0constraints(self):
        return [[250, 500], [1.35, 2.5], [2.8, float('inf')]]
        
    def _DMC1(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 50
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 400
        Keq = 3*(((Tnext/100 - 4)**2 + 1)**(-1)) 
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC1constraints(self):
        return [[350, 600], [4.5, 6], [1.2, float('inf')]]
    
    def _DMC2(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 75
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 450
        Keq = 4*(((Tnext/45 - 10)**2 + 1)**(-1)) 
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC2constraints(self):
        return [[400, 500], [2.5, 5.5], [1.7, float('inf')]]
    
    def _DMC3(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 100
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 420
        Keq = 2*(((Tnext/20 - 21)**2 + 1)**(-1)) 
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC3constraints(self):
        return [[300, 500], [1.0, 3.75], [1.3, float('inf')]]
    
    def _DMC4(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 50
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 450
        Keq = 3*(((Tnext/4.5 - 100)**2 + 1)**(-1))
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC4constraints(self):
        return [[400, 600], [0.5, 5.5], [1.5, float('inf')]]
    
    def _DMC5(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 75
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 350
        Keq = 2.5*(((Tnext/17.5 - 20)**2 + 1)**(-1)) 
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC5constraints(self):
        return [[200, 400], [1.5, 4.5], [1, float('inf')]]
    
    def _DMC6(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 100
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 350
        Keq = 5.5*(((Tnext/35 - 10)**2 + 1)**(-1)) 
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC6constraints(self):
        return [[250, 450], [0.5, 3.5], [3.1, float('inf')]]
    
    def _DMC7(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 50
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 470
        Keq = 1.5*(((Tnext/23.5 - 20)**2 + 1)**(-1))
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC7constraints(self):
        return [[400, 600], [4.5, 6], [1, float('inf')]]
    
    def _DMC8(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 75
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 400
        Keq = 2*(((Tnext/40 - 10)**2 + 1)**(-1))
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC8constraints(self):
        return [[200, 500], [2.5, 5], [1.1, float('inf')]]
    
    def _DMC9(self, inputList, Tset):
        Tcurr = inputList[0]
        P = inputList[1]
        prevKeq = inputList[2]
        
        V = np.pi * 5 * 100
        change = Tset - Tcurr if Tset-Tcurr <= 5 else (Tset - Tcurr)/10
        Tnext = Tcurr + change + (np.random.rand()*10 - 5)
        
        Pnext = (self.R * Tnext) / V + (np.random.rand()*0.02 - 0.01)
        
        # max @ 500
        Keq = 3*(((Tnext/50 - 10)**2 + 1)**(-1))
        Keq = min(Keq, prevKeq)
        return (Tnext, Pnext, Keq)
    
    def DMC9constraints(self):
        return [[400, 600], [1, 3], [1.3, float('inf')]]
    
    
    def getConstraints(self):
        method = getattr(self, f"{self.functionName}constraints", None)
        if callable(method):
            return method()
        else:
            return [[0, 0], [0, 0], [0, 0]]
    
    def update(self, goal, inputList):
        method = getattr(self, f"_{self.functionName}", None)
        if callable(method):
            return method(inputList, goal)
        else:
            return inputList