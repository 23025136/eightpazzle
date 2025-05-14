Time Complexity

Space Complexity

Solution Path Length

Criteria	Breadth-First Search (BFS)	Depth-First Search (DFS)	A* Search Algorithm
Time Complexity	O(b^d)	O(b^d)	O(b^d), improved by good heuristics
Space Complexity	O(b^d) — stores all nodes at a level	O(d) — only tracks current path	O(b^d) — maintains frontier + cost
Path Length	Optimal (shortest)	Not optimal (may find deeper path)	Optimal with admissible heuristic
Guarantees	Completes if solution exists	May fail if depth is too shallow	Always completes (if heuristic is admissible)
Speed (in practice)	Slow on deeper states	Fast on shallow states, fails on deep	Fast and effective on most inputs

Legend:

b = branching factor (~2.13 for 8-puzzle)

d = depth of solution
