from collections import defaultdict


class Graph:

    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)

    # add an edge between two nodes, u and v
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS_Iterative(self, r):
        stack = []

        visited = []
        stack.append(r)

        while stack:

            r = stack.pop()
            if r not in visited:
                visited.append(r)
                for adjacent in reversed(self.graph[r]):
                    stack.append(adjacent)







        print(str(visited))




    def DFS_Recursive(self, r):
        visited = []
        self.search(r, visited)
        print(str(visited))

    def search(self, r, visited):
        visited.append(r)

        for adjacent in self.graph[r]:
            if adjacent not in visited:
                self.search(adjacent, visited)
