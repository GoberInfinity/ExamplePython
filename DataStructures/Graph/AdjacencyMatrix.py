class Graph:
    def __init__(self, num_of_vertex):
        self.num_of_vertex = num_of_vertex
        self.matrix = self.create_adjacency_matrix()

    def create_adjacency_matrix(self):
        return [
            [0 for _ in range(self.num_of_vertex)] for _ in range(self.num_of_vertex)
        ]

    def edge_between(self, a, b):
        self.matrix[a][b] = 1
        self.matrix[b][a] = 1
        return self.matrix


eg = Graph(3)
print(eg.matrix)
print(eg.edge_between(0, 2))
