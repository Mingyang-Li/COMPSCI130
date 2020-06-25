class PriorityQueueInefficient:

    def __init__(self):
        self.__values = []

    def insert(self, key):
        self.__values.append(key)

    def del_min(self):
        smallest = min(self.__values)
        self.__values.remove(smallest)
        return smallest


def is_binary_heap_old(values):
    start = 1
    leftc = start * 2
    rightc = start * 2 + 1
    while start * 2 < len(values)-1 < len(values):
        if leftc >= len(values) or rightc >= len(values) or (values[start] > values[leftc] or values[start] > values[rightc]):
            return False
        start += leftc
        leftc = start * 2
        rightc = start * 2 + 1
    return True


def is_binary_heap(values):
    start = 2
    for i in range(start, len(values), 1):
        if values[i] <= values[i // 2]:
            return False
    return True


class PriorityQueue:
    def __init__(self):
        self.__bin_heap = [0]
        self.__size = 0

    def insert(self, item):
        self.__bin_heap.append(item)
        self.__size += 1
        self.perc_up(self.__size)

    def __str__(self):
        return str(self.__bin_heap)

    def perc_up(self, i):
        while i // 2 > 0:
            if self.__bin_heap[i] < self.__bin_heap[i // 2]:
                self.__bin_heap[i //
                                2], self.__bin_heap[i] = self.__bin_heap[i], self.__bin_heap[i//2]
            i = i // 2

    def get_min_child_index(self, i):
        first = self.__bin_heap[i * 2]
        second = self.__bin_heap[i * 2 + 1]
        smaller = min(first, second)
        if smaller == first:
            return i * 2
        return i * 2 + 1

    def del_min(self):
        return_val = self.__bin_heap[1]
        self.__bin_heap[1] = self.__bin_heap[self.__size]
        self.__size = self.__size - 1
        self.__bin_heap.pop()
        self.perc_down(1)
        return return_val

    def min_child(self, i):
        if i * 2 + 1 > self.__size:
            return i * 2
        else:
            return self.get_min_child_index(i)

    def perc_down(self, i):
        while i * 2 <= self.__size:
            mc = self.min_child(i)
            if self.__bin_heap[i] > self.__bin_heap[mc]:
                self.__bin_heap[mc], self.__bin_heap[i] = self.__bin_heap[i], self.__bin_heap[mc]
            i = mc

    def create_heap_fast(self, values):
        self.__bin_heap = [0] + values
        self.__size = len(values)

        for i in range(self.__size // 2, 0, -1):
            self.perc_down(i)


def create_heap(values):
    pq = PriorityQueue()
    for n in values:
        pq.insert(n)
    return pq


def heap_sort(values):
    pq = PriorityQueue()
    for n in values:
        pq.insert(n)
    array = []
    ct = 0
    while ct < len(values):
        array.append(pq.del_min())
        ct += 1
    return array
