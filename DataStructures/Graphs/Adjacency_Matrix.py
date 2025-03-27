# Graph definition
graph = {
    "Issac": ['Pranay', 'Bharadwaj', "Sulthan", "Suhas"],
    "Bharadwaj": ['Pranay', "Sulthan", "Suhas", "Shasank"],
    "Pranay": ['Bharadwaj', "Sulthan", "Suhas", "Sohail"],
    "Sulthan": ['Pranay', 'Bharadwaj', "Suhas"],
    "Suhas": ['Pranay', 'Bharadwaj', "Sulthan", "Sai"],
    "Shasank":[],
    "Sai":[],
    "Sohail":[]
}

# List of vertices
vertices = list(graph.keys())

# Initialize the adjacency matrix with zeros
n = len(vertices)
adj_matrix = [[0] * n for _ in range(n)]

# Map each vertex to an index
vertex_index = {vertex: idx for idx, vertex in enumerate(vertices)}

# Fill the adjacency matrix
for vertex, neighbors in graph.items():
    for neighbor in neighbors:
        # Set both [vertex][neighbor] and [neighbor][vertex] because it's undirected
        adj_matrix[vertex_index[vertex]][vertex_index[neighbor]] = 1
        adj_matrix[vertex_index[neighbor]][vertex_index[vertex]] = 1  # Symmetric for undirected

# Print the matrix
for row in adj_matrix:
    print(row)
