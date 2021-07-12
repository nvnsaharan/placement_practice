# n = number of nodes in the graph
# G = adjacancy list representing graph
G = []
n = 5
visited = [False for i in range(n)]


def dfs(at):
    if visited[at]:
        return
    visited[at] = True
    neighbours = G[at]
    for next in neighbours:
        dfs(next)


start_node = 0
dfs(start_node)
