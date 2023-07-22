from collections import defaultdict

class Graph:


    def __init__(self):
        #Default dictionary to store the graph
        self.graph = defaultdict(list)

    #add an edge between two nodes, u and v
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #print a breadth first search of Graph
    def BFS(self, r):

        #Mark all nodes as not visited
        visited = [False] * (max(self.graph)+1)

        #new queue
        queue = []

        #visit root node and enqueue it
        queue.append(r)
        visited[r] = True

        while queue:

            #Dequeue a node a print it
            r = queue.pop()
            print(r, end=" ")


            #get all adjacent nodes of the dequeued node, r
            #If not visited mark as visited and enqueue
            for i in self.graph[r]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True



