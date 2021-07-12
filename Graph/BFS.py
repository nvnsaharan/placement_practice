# s = node where to start


def BFS(s, graph):
    visited = [False, ..., False]
    # boolean array for visited size = no. of nodes
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
