def getParent(pos):
    return (pos + 1) // 2 - 1


def getChildren(pos):
    right = (pos + 1) * 2
    left = right - 1
    return left, right


# python is crazy
def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def backtrack(bestParents, start, end):
    if end not in bestParents:
        return None
    cursor = end
    path = [cursor]
    while cursor in bestParents:
        cursor = bestParents[cursor]
        path.append(cursor)
        if cursor == start:
            return list(reversed(path))
    return None


def djikstra(weightedGraph, start, end):
    """
    Calculate the shortest path from start to end in a directed, weighted graph.
    Node can essentially be any hashable data type
    :param weightedGraph: {"node0": {"node1": weight,...},...}
    :param start: starting node
    :param end: node to end at
    :return: ["START",...,"END"] or None if no path exists
    """
    distances = {i: float("inf") for i in weightedGraph}
    bestParents = {i: None for i in weightedGraph}

    toVisit = Heap()
    toVisit.add((0, start))
    distances[start] = 0

    visited = set()

    while toVisit:
        sourceDistance, source = toVisit.pop()
        if sourceDistance > distances[source]:
            continue
        if source == end:
            break
        visited.add(source)
        for target, distance in weightedGraph[source].items():
            if target in visited:
                continue
            newDistance = distances[source] + weightedGraph[source][target]
            if distances[target] > newDistance:
                distances[target] = newDistance
                bestParents[target] = source
                toVisit.add((newDistance, target))

    return backtrack(bestParents, start, end)


class Heap:

    def __init__(self):
        self._array = []

    # show the head of the array
    def peek(self):
        return self._array[0] if self._array else None

    def getSmallestChild(self, parent):
        return min([
            it for it in getChildren(parent)
            if it < len(self._array)
        ], key=lambda it: self._array[it], default=-1)

    def siftDown(self):
        parent = 0
        smallest = self.getSmallestChild(parent)
        while smallest != -1 and self._array[smallest] < self._array[parent]:
            swap(self._array, smallest, parent)
            parent, smallest = smallest, self.getSmallestChild(smallest)

    def pop(self):
        if not self._array:
            return None
        swap(self._array, 0, len(self._array) - 1)
        node = self._array.pop()
        self.siftDown()
        return node

    def siftUp(self):
        index = len(self._array) - 1
        parent = getParent(index)
        while parent != -1 and self._array[index] < self._array[parent]:
            swap(self._array, index, parent)
            index, parent = parent, getParent(parent)

    def add(self, item):
        self._array.append(item)
        self.siftUp()

    def __bool__(self):
        return bool(self._array)
