class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def __str__(self):
        return str(self.__data)

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self, head=None):
        self.__head = head

    def add(self, value):
        newNode = Node(value)
        newNode.set_next(self.__head)
        self.__head = newNode

    def is_empty(self):
        return self.__head == None

    def size(self):
        ct = 0
        curr = self.__head
        while curr != None:
            ct += 1
            curr = curr.get_next()
        return ct

    def __str__(self):
        newStr = ""
        curr = self.__head
        while curr != None:
            newStr += str(curr.get_data())
            newStr += ', '
            curr = curr.get_next()
        return '[{}]'.format(newStr[:-2])

    def remove_from_tail(self):
        if self.__head == None:
            return None
        if self.size() == 1:
            onlyOne = self.__head
            self.__head = None
            return onlyOne

        curr = self.__head
        while curr.get_next().get_next():
            curr = curr.get_next()
        removed = curr.get_next()
        curr.set_next(None)
        return removed

    def remove_from_head(self):
        if self.__head == None:
            return None
        if self.size() == 1:
            onlyOne = self.__head
            self.__head = None
            return onlyOne

        head = self.__head
        self.__head = self.__head.get_next()
        '''
        newStartingNode = self.__head.get_next()
        while newStartingNode.get_next() != None:
            if self.__head == newStartingNode:
                self.__head.set_data(newStartingNode)
            else:
                self.__head.set_next(newStartingNode)
                newStartingNode = newStartingNode.get_next()
                self.__head = self.__head.get_next()
        '''
        return head

    def add_all(self, myList):
        for i in range(0, len(myList)):
            item = myList[i]
            self.add(item)

    def to_list(self):
        newList = []
        curr = self.__head
        while curr != None:
            newList.append(curr.get_data())
            curr = curr.get_next()
        return newList

    def no_duplicate(self):
        curr = self.__head
        prev = None
        itemList = []
        while curr:
            if curr.get_data() in itemList:
                return False
            else:
                itemList.append(curr.get_data())
                prev = curr
            curr = prev.get_next()
        return True

    def search(self, search_value):
        curr = self.__head

        while curr:
            if curr.get_data() == search_value:
                return True
            else:
                curr = curr.get_next()
        return False


class MyNumber:
    def __init__(self, upper_limit):
        self.__upper_limit = upper_limit
        self.__current_number = 1

    def __iter__(self):
        return MyNumberIterator(self.__upper_limit, self.__current_number)


class MyNumberIterator:
    def __init__(self, upper_limit, current_number):
        self.upper_limit = upper_limit
        self.current_number = current_number

    def __next__(self):
        if self.current_number > self.upper_limit:
            raise StopIteration
        else:
            returned = self.current_number
            self.current_number += 1
        return returned


class LinkedListIterator:
    def __init__(self, head):
        self.__current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.__current:
            raise StopIteration
        else:
            returned = self.__current.get_data()
            self.__current = self.__current.get_next()
            return returned

