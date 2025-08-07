import heapq
def dijkstra(graph, start):
    # Set initial distances to infinity for all nodes, except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]
    while priority_queue:
        # Get the node with the smallest distance (pop it from the queue)
        current_distance, current_node = heapq.heappop(priority_queue)
        # If the current distance is already larger than the known shortest distance, skip
        if current_distance > distances[current_node]:
            continue
        # For each neighbor of the current node, update the shortest distance if possible
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If a shorter path to the neighbor is found, update the distance and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
# Input the graph as an adjacency list (dictionary form)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
# Ask the user for the start node
start_node = input("Enter the start node (A, B, C, D): ")
# Run Dijkstra's algorithm
distances = dijkstra(graph, start_node)
# Output the shortest distances from the start node to every other node
print("\nShortest distances from the start node:")
for node, distance in distances.items():
    print(f"Distance from {start_node} to {node}: {distance}")
