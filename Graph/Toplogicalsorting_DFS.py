# Graph is sorted as adjacency list
# Every DAG may have one or more topological orderings.
# Topological sort is not possible if the graph has a cycle.


def topsort(graph):
    N = graph.numberofNodes()
    V = [False, ..., False]  # len N
    order = [0, 0, 0, ..., 0]
    i = N - 1
    for at in range(N):
        if V[at] == False:
            visitedNodes = []
            dfs(at, V, visitedNodes, graph)
            for nodeId in visitedNodes:
                order[i] = nodeId
                i = i - 1
    return order


def dfs(at, V, visitedNodes, graph):
    V[at] = True
    edges = graph.getEdgesOutFronNode(at)
    for edge in edges:
        if V[edge.to] == False:
            dfs(edge.to, V, visitedNodes, graph)
    visitedNodes.add(at)
