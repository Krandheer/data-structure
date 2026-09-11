from collections import deque


def bfs(graph, start):
    visited = set()  # set to keep track of visited vertices
    queue = deque([start])  # queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # visit all adjacent vertices that haven't been visited yet
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

graph_1 = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

bfs(graph_1, "A")
