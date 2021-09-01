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


####### course schedule 2

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        output = []
        visited,cycle = set(),set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
            
        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return output