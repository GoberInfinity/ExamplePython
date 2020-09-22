"""
Depth-first search (DFS) is an algorithm for traversing or searching tree
or graph data structures. One starts at the root (selecting some arbitrary
node as the root in the case of a graph) and explores as far as possible
along each branch before backtracking.
"""
from collections import deque


class Graph:
    def __init__(self):
        self.grap = {}

    def addNode(self, uid):
        self.grap[uid] = None

    def addArc(self, uid, arc):
        self.grap[uid] = arc

    def addGraph(self, graph):
        self.grap = graph

    def getAll(self):
        return self.grap

    def getArc(self, uid):
        return self.grap.get(uid)

    def recursive_dfs(self, start, path):
        path.append(start)
        for node in self.grap[start]:
            if node not in path:
                path = self.recursive_dfs(node, path)
        return path

    def iterative_dfs(self, start, path):
        stack = deque([start])
        while stack:
            node = stack.popleft()
            if node not in path:
                path.append(node)
                stack.extendleft(reversed(self.grap[node]))
        return path

    def iterative_bfs(self, start, path):
        stack = deque([start])
        while stack:
            node = stack.popleft()
            if node not in path:
                path.append(node)
                stack.extend(self.grap[node])
        return path

    def find_path(self, start, end, path):
        path = path + [start]
        if start == end:
            return path
        if start not in self.grap:
            return None
        for node in self.grap[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_all_path(self, start, end, path):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.grap:
            return []
        paths = []
        for node in self.grap[start]:
            if node not in path:
                newpaths = self.find_all_path(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


graph_eg = Graph()
graphTree = Graph()

graph_eg.addGraph(
    {"A": ["B", "C"], "B": ["D", "E"], "C": ["D", "E"], "D": ["E"], "E": ["A"]}
)
graphTree.addGraph({1: [2, 3], 2: [4, 5], 4: [2], 5: [2], 3: [1]})

print(graph_eg.recursive_dfs("A", []))
print(graph_eg.iterative_dfs("A", []))
print(graph_eg.find_path("A", "E", []))
print(graph_eg.find_all_path("A", "E", []))
print(graphTree.recursive_dfs(1, []))
print(graphTree.iterative_dfs(1, []))
print(graphTree.iterative_bfs(1, []))
