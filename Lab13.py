'''Q1-Q5'''


class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        if len(self.__items) <= 0:
            raise IndexError('The queue is empty!')
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        if len(self.__items) <= 0:
            raise IndexError('The queue is empty!')
        return self.__items[len(self.__items)-1]

    def multi_dequeue(self, number):
        if number < len(self.__items):
            return False
        for i in range(number):
            self.dequeue()
            i = i
        return True

    def to_list(self):
        return [self.__items[i] for i in range(len(self.__items)-1, -1, -1)]

    def splice(self, second_queue):
        listed2ndQueue = second_queue.to_list()
        for n in listed2ndQueue:
            self.enqueue(n)

    def enqueue_list(self, a_list):
        for item in a_list:
            self.enqueue(item)

    def __str__(self):
        return 'Queue: ' + str(self.__items[::-1])


'''q6'''


def countup_queue(number):
    newQueue = Queue()
    while number > 0:
        newQueue.enqueue(number)
        number -= 1
    return newQueue


'''q7'''


def get_front_of_queue(a_queue):
    if a_queue.is_empty():
        return None
    return a_queue.peek()


'''q8'''


def exchange_queue(queue1, queue2):
    size1 = queue1.size()
    size2 = queue2.size()
    q1Count = 0
    while q1Count < size1:
        queue2.enqueue(queue1.dequeue())
        q1Count += 1

    q2Count = 0
    while q2Count < size2:
        queue1.enqueue(queue2.dequeue())
        q2Count += 1


'''q9'''


def mirror_queue(myQueue):
    stack = []
    qLen = myQueue.size()
    while myQueue.size() != 0:
        stack.append(myQueue.dequeue())

    i = 0
    while myQueue.size() < qLen:
        myQueue.enqueue(stack[i])
        i += 1

    i = len(stack) - 1
    while myQueue.size() < qLen * 2:
        myQueue.enqueue(stack[i])
        i -= 1


'''q10'''


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: ' + str(self.__items)


def is_palindrome(word):
    newStack = Stack()
    newQueue = Queue()
    for c in word:
        newStack.push(c)
        newQueue.enqueue(c)

    if newStack.size() != newQueue.size():
        return False

    minLen = min(newQueue.size(), newStack.size())
    for i in range(minLen // 2):
        i = i
        if newStack.pop() != newQueue.dequeue():
            return False
    return True
