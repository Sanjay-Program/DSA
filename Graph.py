def create_adjacency_matrix(num_nodes, edges):
    # Initialize a num_nodes x num_nodes matrix with zeros
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    # Fill the matrix based on the edges
    for (start, end) in edges:
        adjacency_matrix[start][end] = 1  # For directed graph
        # adjacency_matrix[end][start] = 1  # Uncomment for undirected graph

    return adjacency_matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage
num_nodes = 5  # Number of nodes in the graph
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]  # List of edges

adjacency_matrix = create_adjacency_matrix(num_nodes, edges)
display_matrix(adjacency_matrix)
