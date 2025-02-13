import numpy as np
    """
    
    
        NOT DONE YET!!!
    
    
    """
class DMC_structure:
    def __init__(self, graph, functionNames, goals):
        """_summary_

        Args:
            graph (_type_): a graph of nodes. DMC's labeled in numerical order
            functionNames (_type_): list of functionNames in numerical order;
            goals (_type_): list of goals in numerical order
        """
        self.graph = graph
        self.goals = goals
        self.functionNames = functionNames
        self.initialized = False
    
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            if(self.initialized == False) {
                
            }
            
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        
    