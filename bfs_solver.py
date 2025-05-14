def bfs(start):
    frontier = deque([start])
    came_from = {}
    visited = set()
    visited.add(start)

    while frontier:
        current = frontier.popleft()
        if current == GOAL_STATE:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                frontier.append(neighbor)
    return None
