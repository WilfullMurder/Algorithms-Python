import BinarySearch
from BreadthFirstSearch import Graph as BFS
from DepthFirstSearch import Graph as DFS
from Djikstra import djikstra
from BellmanFord import Graph
from SelectionSort import SelectionSort
from Quicksort import Quicksort


def main():
    g = Graph(5)
    g.addEdges(0,1,2)
    g.addEdges(0,2,4)
    g.addEdges(1,3,2)
    g.addEdges(2,4,3)
    g.addEdges(2,3,4)
    g.addEdges(4,3,-5)

    g.bellmanFord(0)

if __name__ == '__main__':
    main()
