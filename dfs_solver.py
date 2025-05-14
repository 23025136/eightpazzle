def dfs(start, depth_limit=30):
    stack = [(start, 0)]
    came_from = {}
    visited = set()
    
    while stack:
        current, depth = stack.pop()
        if current == GOAL_STATE:
            return reconstruct_path(came_from, current)
        if depth < depth_limit:
            visited.add(current)
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    came_from[neighbor] = current
                    stack.append((neighbor, depth + 1))
    return None
