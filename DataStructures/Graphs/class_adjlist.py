class GraphAdjList:
    def __init__(self):
        self.list = {}

    def add_vertex(self, vertex):
        if vertex not in self.list:
            self.list[vertex] = []
            print(f"{vertex} added")
            return
        else:
            print(f"{vertex} already present")

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.list:
            self.add_vertex(vertex1)
        if vertex2 not in self.list:
            self.add_vertex(vertex2)
        self.list[vertex1].append(vertex2)
        self.list[vertex2].append(vertex1)
        print(f"Edge added between {vertex1} and {vertex2}")

    def remove_edge(self, vertex1, vertex2):
        if vertex2 not in self.list or vertex1 not in self.list:
            print("One or more vertices are missing")
        else:
            if vertex1 in self.list[vertex2]:
                self.list[vertex2].remove(vertex1)
            if vertex2 in self.list[vertex1]:
                self.list[vertex1].remove(vertex2)
            print(f"Edge removed between {vertex1} and {vertex2}")

    def remove_vertex(self, vertex):
        if vertex in self.list:
            for neighbor in list(self.list[vertex]):
                self.list[neighbor].remove(vertex)
            del self.list[vertex]
            print(f"{vertex} removed")

    def display(self):
        for vertex, edges in self.list.items():
            print(f"{vertex}: {edges}")


# Creating a graph instance
graph = GraphAdjList()

# Adding vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

# Adding edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')

# Display the graph
print("\nGraph after adding vertices and edges:")
graph.display()

# Removing an edge
graph.remove_edge('A', 'B')

# Display the graph after removing an edge
print("\nGraph after removing edge A-B:")
graph.display()

# Removing a vertex
graph.remove_vertex('C')

# Display the graph after removing vertex C
print("\nGraph after removing vertex C:")
graph.display()
