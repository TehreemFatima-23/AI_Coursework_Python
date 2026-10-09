import heapq

# Goal State definition (0 represents the blank tile)
GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0)

# Initial State given in the lab task
INITIAL_STATE = (1, 2, 3, 
                 4, 0, 6, 
                 7, 5, 8)


def get_heuristic(state):
    # Calculates h(n): number of misplaced tiles (excluding blank tile 0).
    misplaced = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            misplaced += 1
    return misplaced


def get_neighbors(state):
    # Generates all valid moves (Up, Down, Left, Right) from the current state.
    neighbors = []
    zero_idx = state.index(0)
    row = zero_idx // 3
    col = zero_idx % 3

    # Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_idx = new_row * 3 + new_col
            state_list = list(state)
            # Swap blank space with neighbor
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))

    return neighbors


def print_board(state):
    # Prints the puzzle in a 3x3 grid format.
    for i in range(0, 9, 3):
        row = [str(tile) if tile != 0 else " " for tile in state[i:i+3]]
        print(" | ".join(row))
    print("-" * 9)


def GBFS():
    # Executes Greedy Best-First Search
    counter = 0
    frontier = []
    initial_h = get_heuristic(INITIAL_STATE)
    
    # Priority Queue stores: (heuristic value, tie breaker counter, path taken)
    heapq.heappush(frontier, (initial_h, counter, [INITIAL_STATE]))
    visited = set()

    while frontier:
        h, counter, path = heapq.heappop(frontier)
        current = path[-1]

        if current in visited:
            continue
        visited.add(current)

        # Check if Goal State is reached
        if current == GOAL_STATE:
            print("------8-Puzzle Using GBFS but input in given------")
            print("Sequence of states from start to goal:\n")
            for step, state in enumerate(path):
                print(f"Step {step} (Heuristic h(n) = {get_heuristic(state)}):")
                print_board(state)

            print(f"Total number of steps in solution: {len(path) - 1}")
            return

        # Expand neighbors
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                counter += 1
                neighbor_h = get_heuristic(neighbor)
                heapq.heappush(frontier, (neighbor_h, counter, path + [neighbor]))

GBFS()
