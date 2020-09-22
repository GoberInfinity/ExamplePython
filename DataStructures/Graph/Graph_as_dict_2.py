from collections import defaultdict


def recursive_dfs(graph, start, path):
    """recursive depth first search from start"""
    path = path + [start]
    for node in graph[start]:
        if node not in path:
            path = recursive_dfs(graph, node, path)
    return path


def iterative_dfs(graph, start, path):
    """iterative depth first search from start"""
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = graph[v] + q
    return path


def iterative_bfs(graph, start, path):
    """iterative breadth first search from start"""
    q = [start]
    while q:
        print(q)
        v = q.pop(0)
        print(v)

        if v not in path:
            path = path + [v]
            q = q + graph[v]
    return path


"""
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
"""
graphEg = {"A": ["B", "C"], "B": ["D", "E"], "C": ["D", "E"], "D": ["E"], "E": ["A"]}
g = {1: [2, 3], 2: [4, 5], 4: [2], 5: [2], 3: [1]}
print(iterative_bfs(g, 1, []))


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)
        print(stack)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            print(visited)
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)


g.topologicalSort()
