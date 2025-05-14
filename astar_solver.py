scrambles = [
    (1, 2, 3, 4, 5, 6, 0, 7, 8),  # Easy (2 moves)
    (7, 2, 4, 5, 0, 6, 8, 3, 1),  # Hard (Max difficulty for 8-puzzle)
]

for puzzle in scrambles:
    print("\nInitial Puzzle:", puzzle)

    print("\n→ BFS:")
    bfs_path = bfs(puzzle)
    print("Moves:", len(bfs_path) - 1 if bfs_path else "No solution")

    print("\n→ DFS:")
    dfs_path = dfs(puzzle)
    print("Moves:", len(dfs_path) - 1 if dfs_path else "No solution or timeout")

    print("\n→ A*:")
    astar_path = a_star(puzzle)
    print("Moves:", len(astar_path) - 1 if astar_path else "No solution")
