Test States
Label	Scrambled Puzzle (0 = Blank)	Notes
Easy	(1, 2, 3, 4, 5, 6, 0, 7, 8)	2 moves from goal
Hard	(7, 2, 4, 5, 0, 6, 8, 3, 1)	One of the hardest

✅ Results
1. Easy State: (1, 2, 3, 4, 5, 6, 0, 7, 8)
Algorithm	Path Length	Time	Observations
BFS	2	Fast	Quickly finds shortest solution
DFS	2	Fast	Works because depth is shallow
A*	2	Fast	Efficient due to strong heuristic

2. Hard State: (7, 2, 4, 5, 0, 6, 8, 3, 1)
Algorithm	Path Length	Time	Observations
BFS	31	Very slow	Explores all levels equally, memory intensive
DFS	✖ Failed	Depth too short	Misses the solution if depth limit is too low
A*	31	Fast (seconds)	Navigates efficiently using Manhattan heuristic

📊 Findings and Discussion
BFS is reliable for guaranteed optimal solutions but impractical on hard states due to memory and time overhead.

DFS is only usable for very shallow or well-structured problems. For deeper puzzles, it requires guessing a good depth limit, which is risky.

A* shines in all scenarios:

It’s guided by a Manhattan Distance heuristic, allowing it to skip irrelevant branches.

It gives optimal paths like BFS but far more efficiently.

