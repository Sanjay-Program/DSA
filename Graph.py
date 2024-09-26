#This is a graph using adjacency matrix
def create_adjacency_matrix(num_nodes, edges):
    adjacency_matrix = [[0] * num_nodes for i in range(num_nodes)]
    for (start, end) in edges:
        adjacency_matrix[start][end] = 1 
    return adjacency_matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
edges=[]
c=int(input("Enter the no of connections:"))
for i in range(c):

    a=list(map(int,input("Enter the edges by space:").split(" ")))
    edges.append(a)

adjacency_matrix = create_adjacency_matrix(c,edges)
display_matrix(adjacency_matrix)
