class SelectionSort:

    def findSmallest(self, arr):
        smallest = arr[0]
        smallestIndex = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallestIndex = i
        return smallestIndex

    def sort(self, arr):
        newArr = []
        for i in range(len(arr)):
            smallest = self.findSmallest(self, arr)
            newArr.append(arr.pop(smallest))
        return newArr
