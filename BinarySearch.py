class BinarySearch:

    @staticmethod
    def search(listToSearch, item):
        low = 0
        high = len(listToSearch) - 1

        while low <= high:
            mid = low + high
            guess = listToSearch[mid]
            if guess == item:
                return mid
            if guess < item:
                low = mid + 1
            else:
                high = mid - 1
        return None
