class GraphAdjMatrix:
    def __init__(self, size):
        self.matrix = [[0]*size for _ in range(size)]
        self.vertices = {}
        self.vertices_count = 0
    def add_vertices(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = self.vertices_count
            self.vertices_count += 1
            return f"{vertex} Added"
        else:
            return f"{vertex} already present in graph"
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            return self.add_vertices(vertex1)
        if vertex2 not in self.vertices:
            return self.add_vertices(vertex2)
        if vertex1 in self.vertices and vertex2 in self.vertices:
            index1 = self.vertices[vertex1]
            index2 = self.vertices[vertex2]
            self.matrix[index1][index2] = 1
            self.matrix[index2][index1] = 1
            print(f"Edge Added between {vertex1} amd {vertex2}")
            return
    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            print("one of edge is not present")
            return
        if vertex1 in self.vertices and vertex2 in self.vertices:
            index1 = self.vertices[vertex1]
            index2 = self.vertices[vertex2]
            self.matrix[index1][index2] = 0
            self.matrix[index2][index1] = 0
            print(f"Edge Removed between {vertex1} amd {vertex2}")
            return
    def display(self):
        print("  ", "  ".join(self.vertices))
        for vertex, idx in self.vertices.items():
            print(vertex, self.matrix[idx])

graph_matrix = GraphAdjMatrix(5)
graph_matrix.add_vertices('A')
graph_matrix.add_vertices('B')
graph_matrix.add_vertices('C')
graph_matrix.add_vertices('D')
graph_matrix.add_vertices('E')
graph_matrix.add_edge('A', 'B')
graph_matrix.add_edge('A', 'C')
graph_matrix.add_edge('A', 'D')
graph_matrix.add_edge('C', 'E')
graph_matrix.add_edge('D', 'E')
graph_matrix.display()
