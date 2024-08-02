def best_first_search(graph, start, goal):
    visited = set()
    heap = [(0, start)]  # Priority queue with (heuristic, node)
    while heap:
        (cost, node) = heap.pop(0)  # Get node with minimum heuristic value
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return visited
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors.items():
            if neighbor not in visited:
                heap.append((neighbor_cost, neighbor))  # Add neighbors to queue with their heuristic values
        heap.sort()  # Sort based on heuristic values
    return None

# Example graph
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 1, 'F': 2},
    'D': {'B': 3},
    'E': {'B': 1, 'F': 3},
    'F': {'C': 2, 'E': 3}
}

start_node = 'A'
goal_node = 'F'
result = best_first_search(graph, start_node, goal_node)
if result:
    print("Path found:", ' -> '.join(result))
else:
    print("Path not found")
