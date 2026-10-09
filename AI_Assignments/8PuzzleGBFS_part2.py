import heapq

GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0)


def get_heuristic(state):
    # Calculates h(n): misplaced tiles (excluding tile 0).
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL_STATE[i])


def get_neighbors(state):
    # Generates valid neighbor states.
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_zero_idx = r * 3 + c
            state_list = list(state)
            state_list[zero_idx], state_list[new_zero_idx] = state_list[new_zero_idx], state_list[zero_idx]
            neighbors.append(tuple(state_list))

    return neighbors


def print_board(state):
    # Prints the 3x3 puzzle board.
    for i in range(0, 9, 3):
        row = [str(tile) if tile != 0 else " " for tile in state[i:i+3]]
        print(" | ".join(row))
    print("-" * 9)


def count_inversions(state):
    # Counts inversions ignoring the blank tile (0).
    tiles_only = [tile for tile in state if tile != 0]
    inversions = 0
    for i in range(len(tiles_only)):
        for j in range(i + 1, len(tiles_only)):
            if tiles_only[i] > tiles_only[j]:
                inversions += 1
    return inversions


def is_solvable(state):
    # 8-puzzle is solvable if its inversion count is even.
    return count_inversions(state) % 2 == 0


def applyGBFS():
    # Executes by Handling user input, solvability test, and search.
    print("----- 8-Puzzle Using GBFS by getting input from user -----")
    print("Enter 9 numbers (0 to 8) separated by spaces for the start state.")
    print("Example: 1 2 3 4 6 7 0 5 8")
    
    user_input = input("Start State = ").strip().split()
    initial_state = tuple(int(x) for x in user_input)

    print("\nInitial State Entered:")
    print_board(initial_state)

    # Checking Solvability
    inversion_count = count_inversions(initial_state)
    print(f"Calculated Inversion Count: {inversion_count}")

    if not is_solvable(initial_state):
        print("Status: The puzzle is NOT SOLVABLE! (Odd inversion count). Search aborted.")
        return

    print("Status: The puzzle is SOLVABLE.\n")

    # Greedy Best-First Search
    counter = 0
    frontier = []
    initial_h = get_heuristic(initial_state)
    heapq.heappush(frontier, (initial_h, counter, [initial_state]))
    visited = set()

    while frontier:
        h, counter, path = heapq.heappop(frontier)
        current = path[-1]

        if current in visited:
            continue
        visited.add(current)

        if current == GOAL_STATE:
            print("Solution Found, so the next steps are: \n")
            for step, state in enumerate(path):
                print(f"Step {step} (Heuristic h(n) = {get_heuristic(state)}):")
                print_board(state)

            print(f"Total number of steps in solution are: {len(path) - 1}")
            return

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                counter += 1
                neighbor_h = get_heuristic(neighbor)
                heapq.heappush(frontier, (neighbor_h, counter, path + [neighbor]))
applyGBFS()
