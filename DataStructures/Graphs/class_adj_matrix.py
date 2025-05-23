class Graph:
    def __init__(self, size):
        self.matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.vertices = ['']*size

    def add_vertex(self,idx, vertex):
        if 0 <= idx <= self.size:
            self.vertices[idx]=vertex
            print(f"{vertex} added at {idx}")

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1, idx2 = 0,0
            for i in range(len(self.vertices)):
                if self.vertices[i] == vertex1:
                    idx1 = i
                if self.vertices[i] == vertex2:
                    idx2 = i
            self.matrix[idx1][idx2] = 1
            self.matrix[idx2][idx1] = 1
            print(f"{vertex1} and {vertex2} are connected")
    def print_graph(self):
        print("Adjancency Matrix: ")
        for row in self.matrix:
            print(' '.join(map(str, row)))
        print("Vertex data: ")
        for idx, vertex in enumerate(self.vertices):
            print(f"index {idx}: Vertex : {vertex}")

g = Graph(4)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')
g.add_vertex(3,'D')
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','C')
g.print_graph()


