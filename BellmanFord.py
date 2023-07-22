class Graph:
    def __init__(self, vertices):
        self.M = vertices
        self.graph = []

    def addEdges(self, a, b, c):
        self.graph.append([a, b, c])

    def printSolution(self, distance):
        print("vertex distance from source: ")
        for i in range(self.M):
            print("{0}\t\t{1}".format(i, distance[i]))

    def bellmanFord(self, source):
        distance = [float("inf")] * self.M
        distance[source] = 0

        for _ in range(self.M - 1):
            for s, d, w in self.graph:
                if distance[s] != float("inf") and distance[s] + w < distance[d]:
                    distance[d] = distance[s] + w

        for s, d, w in self.graph:
            if distance[s] != float("inf") and distance[s] + w < distance[d]:
                print("Graph contains negative weight cycle")
                return

        self.printSolution(distance)
