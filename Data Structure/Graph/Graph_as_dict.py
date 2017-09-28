# -*- coding: utf-8 -*-
"""
Depth-first search (DFS) is an algorithm for traversing or searching tree
or graph data structures. One starts at the root (selecting some arbitrary 
node as the root in the case of a graph) and explores as far as possible 
along each branch before backtracking. 
"""
class Graph:
    def __init__(self):
        self.grap = {}
    
    def addNode(self,id):
        self.grap[id] = None
        
    def addArc(self,id,arc):
        self.grap[id] = arc
                 
    def addGraph(self,graph):
        self.grap = graph
    
    def getAll(self):
        return self.grap

    def getArc(self,id):
        return self.grap.get(id)

    def recursive_dfs(self, start, path):
      path.append(start) 
      for node in self.grap[start]:
        if not node in path:
          path= self.recursive_dfs(node, path)
      return path      

graph = Graph()
graphTree = Graph()

graph.addGraph({'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']})
graphTree.addGraph({1:[2,3], 2:[4,5],4:[2],5:[2],3:[1]})
 
print (graph.recursive_dfs('A',[])) 
print (graphTree.recursive_dfs(1,[]))