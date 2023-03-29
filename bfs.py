from collections import deque


def bfs(graph, start):
    visited = set()  # set to keep track of visited vertices
    queue = deque([start])  # queue for BFS
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        # visit all adjacent vertices that haven't been visited yet
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
