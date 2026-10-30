graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

def dfs(graph, start, goal):
    stack = [start]
    visited = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            if current == goal:
                return visited

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

print(dfs(graph, 'A', 'D'))