import heapq  # For priority queue (min-heap)

def prims_algorithm(graph, start_node):
    mst = []  # Store edges of the Minimum Spanning Tree
    visited = set()  # Track visited nodes
    min_heap = [(0, start_node, None)]  # (edge_weight, current_node, parent_node)

    while len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue  # Skip nodes already added to MST

        visited.add(node)

        if parent is not None:
            mst.append((parent, node, weight))  # Add edge to MST

        # Check neighbors
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst

# Define the graph (adjacency list format)
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 6), ('E', 5)],
    'C': [('A', 3), ('B', 1), ('E', 5)],
    'D': [('B', 6), ('E', 4)],
    'E': [('B', 5), ('C', 5), ('D', 4)]
}

# Run the algorithm from starting node 'A'
mst = prims_algorithm(graph, 'A')

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"{edge[0]} -- {edge[2]} --> {edge[1]}")
