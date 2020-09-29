"""
bfs and dfs don't handle orphan nodes &
nodes that are not reachable by the starting point but are connected to the graph,
to solve that issue iterate through all the number of nodes
and after that call bfs or dfs (check how topological sort does the trick)
"""
from collections import defaultdict, deque


class Graph:
    def __init_(self):
        self.graph = defaultdict(list)

    def create_graph_from(self, dict_graph):
        self.graph = dict_graph

    def add_edge_between(self, a, b):
        self.graph[a].append(b)

    def recursive_dfs(self, start, path, visited):
        visited[start] = True
        path.append(start)
        for forward_node in self.graph[start]:
            if not visited[forward_node]:
                path = self.recursive_dfs(forward_node, path, visited)
        return path

    def iterative_dfs(self, start, path, visited):
        nodes = deque([start])
        while nodes:
            layer_node = nodes.popleft()
            if not visited[layer_node]:
                visited[layer_node] = True
                path.append(layer_node)
                nodes.extendleft(reversed(self.graph[layer_node]))
        return path

    def bfs(self, start, path, visited):
        nodes = deque([start])
        while nodes:
            layer_node = nodes.popleft()
            if not visited[layer_node]:
                visited[layer_node] = True
                path.append(layer_node)
                nodes.extend(self.graph[layer_node])
        return path

    def find_path_between(self, start, end, path, visited):
        if start not in self.graph:
            return None

        # Adds two lists and produces a new list
        path += [start]
        visited[start] = True
        if start == end:
            return path

        for next_node in self.graph[start]:
            if not visited[next_node]:
                if complete_path := self.find_path_between(
                    next_node, end, path, visited
                ):
                    return complete_path
        return None

    def topological_sort(self, start, path, visited):
        for node in self.graph:
            if not visited[node]:
                self._topological_sort_util(node, path, visited)
        return path

    def _topological_sort_util(self, start, path, visited):
        visited[start] = True
        for node in self.graph[start]:
            if not visited[node]:
                self.topological_sort(node, path, visited)
        path.appendleft(start)


eg = Graph()
cyclic_graph = {1: [2, 3], 2: [4, 5], 4: [2], 5: [2], 3: [1]}
acyclic_graph = {5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}

eg.create_graph_from(cyclic_graph)

path = []
visited_nodes = [False] * (max(eg.graph) + 1)
print(eg.recursive_dfs(1, path, visited_nodes))

path = []
visited_nodes = [False] * (max(eg.graph) + 1)
print(eg.iterative_dfs(1, path, visited_nodes))

path = []
visited_nodes = [False] * (max(eg.graph) + 1)
print(eg.bfs(1, path, visited_nodes))

path = []
visited_nodes = [False] * (max(eg.graph) + 1)
print(eg.find_path_between(1, 5, path, visited_nodes))

eg.create_graph_from(acyclic_graph)
topological_sorted = deque()
visited_nodes = [False] * (max(eg.graph) + 1)
print(eg.topological_sort(5, topological_sorted, visited_nodes))
