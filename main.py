from collections import deque
import heapq

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = {
    'UP': -3,
    'DOWN': 3,
    'LEFT': -1,
    'RIGHT': 1
}

def get_neighbors(state):
    neighbors = []
    index = state.index(0)

    def is_valid(pos):
        if pos < 0 or pos >= 9:
            return False
        if index % 3 == 0 and pos % 3 == 2:
            return False
        if index % 3 == 2 and pos % 3 == 0:
            return False
        return True

    for move, offset in MOVES.items():
        new_index = index + offset
        if is_valid(new_index):
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]
