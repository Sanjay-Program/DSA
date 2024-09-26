#This is a graph using adjacency matrix
def create_adjacency_matrix(num_nodes, edgees):
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for (start, end) in edges:
        adjacency_matrix[start][end] = 1 
    return adjacency_matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
num_nodes = 5  
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]  
adjacency_matrix = create_adjacency_matrix(num_nodes, edges)
display_matrix(adjacency_matrix)
