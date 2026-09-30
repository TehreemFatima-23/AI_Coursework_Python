# Graph of the maze in the form of numbers
graph = {
    1: [2, 7],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6, 26],
    6: [5, 17],

    7: [1, 8],
    8: [7, 9],
    9: [8, 10],
    10: [9, 11],
    11: [10, 12],
    12: [11, 13],

    13: [12, 14, 25],
    14: [13, 15],
    15: [14, 16],
    16: [15, 20],

    17: [6, 18],
    18: [17, 19, 21],
    19: [18, 20],
    20: [19, 16, 22],

    21: [18],
    22: [20],

    23: [24],
    24: [23, 25],
    25: [24, 13],

    26: [5]
}

# BFS function to solve this maze puzzle
def bfs(graph, start, goal):

    queue = [start]

    visited = {start}

    parent = {start: None}

    while queue:

        current = queue.pop(0)

        print("The current node (Visiting): ", current)

        if current == goal:
            break

        for neighbor in graph[current]:

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)


    # Create the final path
    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parent[current]

    path.reverse()

    return path


# Starting and goal nodes
start = 23
goal = 26

print("Start Node is: ", start)
print("Goal Node is: ", goal)

path = bfs(graph, start, goal)

print("\nShortest path using BFS:")
print(path)