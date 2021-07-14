# A complete binary tree that
# satisfies a heap's property

# for max heap

# for heap sort use delete n times to get max
# element and then reverse O(n * logn)


class Heap:
    def __init__(self):
        self.arr = [None]

    def buildheap(self, A):
        self.arr[1:] = A
        for i in range(len(A) // 2):
            self.heapify(1)

    def heapify(self, i):
        # call heapify on i
        # call this fxn on all elemts of array
        # O(logn)
        largest = i
        left = 2 * i
        right = 2 * i + 1
        if self.arr[left] > self.arr[largest]:
            larger = left
        if self.arr[right] > self.arr[largest]:
            larger = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)  # to recurse

    def insert(self, value):
        # O(logn)
        self.arr.append(value)
        i = len(self.arr)
        while i > 1:
            parent = i // 2
            if self.arr[parent] < self.arr[i]:
                self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
                i = parent
            else:
                return True
        return True

    def makeheap(self, A):
        # using insert fxn in O(n*logn)
        for i in A:
            self.insert(i)

    # only root node is deletable
    def delete(self):
        # O(logn)
        self.arr[1] = self.arr[-1]
        self.arr.pop()
        i = 1
        while i < len(self.arr):
            left = self.arr[2 * i]
            right = self.arr[2 * i + 1]
            if left > right:
                larger = 2 * i
            else:
                larger = 2 * i + 1
            if self.arr[i] < self.arr[larger]:
                self.arr[i], self.arr[larger] = self.arr[larger], self.arr[i]
                i = larger
            else:
                return
