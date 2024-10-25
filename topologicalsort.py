# Function to perform topological sort using in-degree count
def topological_sort(vertices, edges):
    # Step 1: Initialize in-degree of all vertices to 0
    in_degree = [0] * vertices
    adj_list = [[] for _ in range(vertices)]
    
    # Step 2: Build the adjacency list and calculate in-degrees
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1
    
    # Step 3: Collect all vertices with 0 in-degree
    result = []
    zero_in_degree = [i for i in range(vertices) if in_degree[i] == 0]
    
    # Step 4: Process all vertices with 0 in-degree
    while zero_in_degree:
        # Remove vertex with 0 in-degree and add to result
        u = zero_in_degree.pop(0)  # Simulate a queue by removing the first element
        result.append(u)
        
        # Decrease in-degree for adjacent vertices
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:  # Add to zero_in-degree list if in-degree becomes 0
                zero_in_degree.append(v)
    
    # Step 5: Return the topological order
    if len(result) == vertices:
        return result
    else:
        return "Graph has a cycle, topological sort not possible."

# Input number of vertices and edges
vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Input edges
edges = []
for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u v): ").split())
    edges.append((u, v))

# Perform topological sort
print("Topological Sort:", topological_sort(vertices, edges))
