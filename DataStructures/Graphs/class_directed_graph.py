class Graph:
    def __init__(self, size):
        self.matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.vertices = ['']*size

    def add_vertex(self,idx, vertex):
        if 0 <= idx <= self.size:
            self.vertices[idx]=vertex
            print(f"{vertex} added at {idx}")

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1, idx2 = 0,0
            for i in range(len(self.vertices)):
                if self.vertices[i] == vertex1:
                    idx1 = i
                if self.vertices[i] == vertex2:
                    idx2 = i
            self.matrix[idx1][idx2] = weight
            print(f"{vertex1} and {vertex2} are connected with weight {weight}")
    def print_graph(self):
        print("Adjancency Matrix: ")
        for row in self.matrix:
            print(' '.join(map(str, row)))
        print("Vertex data: ")
        for idx, vertex in enumerate(self.vertices):
            print(f"index {idx}: Vertex : {vertex}")
    def dfs(self, vertex):
        visited = set()
        if vertex in self.vertices:
            start_idx = self.vertices.index(vertex)
            print(f"DFS starting from : {start_idx} - {vertex}")
            self.dfs_util(start_idx, visited)
            print()
        else:
            print(f"Vertex {vertex} not found in graph")
    def dfs_util(self, crt_idx, visited):
        crt_vtx = self.vertices[crt_idx]
        print(crt_vtx, end = " ")
        visited.add(crt_vtx)
        for neighbor_idx in range(self.size):
            if self.matrix[crt_idx][neighbor_idx] !=0 and self.vertices[neighbor_idx] not in visited:
                self.dfs_util(neighbor_idx, visited)
    def bfs(self, vertex):
        visited = set()
        queue = []
        if vertex in self.vertices:
            vertex_idx = self.vertices.index(vertex)
            visited.add(vertex_idx)
            queue.append(vertex_idx)
            print(f"BFS starting from {vertex} - {vertex_idx}")
            while queue:
                current_idx = queue.pop(0)
                print(self.vertices[current_idx], end = "  ")
                for neighbor_idx in range(self.size):
                    if self.matrix[current_idx][neighbor_idx]!=0 and neighbor_idx not in visited:
                        queue.append(neighbor_idx)
                        visited.add(neighbor_idx)
            print()
        else:
            print(f"{vertex} not found in graph")




g = Graph(4)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')
g.add_vertex(3,'D')
g.add_edge('A','B',3)
g.add_edge('A','C',2)
g.add_edge('D','A',4)
g.add_edge('C','B',1)
g.print_graph()


print("New Graph")
g = Graph(7)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')
g.add_vertex(3,'D')
g.add_vertex(4,'E')
g.add_vertex(5,'F')
g.add_vertex(6,'G')

g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'E', 1)
g.add_edge('C', 'F', 1)
g.add_edge('F', 'G', 1)


g.dfs('A')
g.bfs('C')
