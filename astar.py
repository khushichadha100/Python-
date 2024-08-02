def a_star(graph, start, goal, heuristic):
    open_set = {start}
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])
        
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path
        
        open_set.remove(current)
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Example graph
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 1, 'F': 2},
    'D': {'B': 3},
    'E': {'B': 1, 'F': 3},
    'F': {'C': 2, 'E': 3}
}

# Heuristic values for each node (estimated distance to goal)
heuristic = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 0
}

start_node = 'A'
goal_node = 'F'
result = a_star(graph, start_node, goal_node, heuristic)
if result:
    print("Path found:", ' -> '.join(result))
else:
    print("Path not found")

