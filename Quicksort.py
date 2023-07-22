class Quicksort:
    def quicksort(self, arr):
        if len(arr) < 2:
            return arr  # base case
        else:
            pivot = arr[0]  # recursive case
            lessThan = [i for i in arr[1:] if i <= pivot]  # subset of all elements less than or equal to pivot
            moreThan = [i for i in arr[1:] if i > pivot]  # subset of all elements more than pivot

            return self.quicksort(self, lessThan) + [pivot] + self.quicksort(self, moreThan)

