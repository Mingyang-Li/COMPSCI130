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

    def add_after(self, value):
        currNext = self.__next
        newNode = Node(value)
        self.set_next(newNode)
        newNode.set_next(currNext)

    def remove_after(self):
        self.set_next(self.__next.__next)


def create_sample_node_chain():
    first = Node('three')
    second = Node('linked')
    last = Node('nodes')
    first.set_next(second)
    second.set_next(last)
    return first


def create_node_chain(newList):
    if len(newList) == 1:
        return Node(newList[0])
    else:
        first = Node(newList[0])
        second = Node(newList[1])
        for i in range(0, len(newList)-1):
            if i == 0:
                first.set_next(second)
            else:
                nextNode = Node(newList[i+1])
                if i == 1:
                    second.set_next(nextNode)
                elif i == 2:
                    second.get_next().set_next(nextNode)
                elif i == 3:
                    second.get_next().get_next().set_next(nextNode)
        return first


def convert_to_list(myNode):
    newList = []
    if myNode.get_next() == None:
        newList.append(myNode.get_data())
    while myNode.get_next() != None:
        currnode = myNode.get_data()
        newList.append(currnode)
        myNode = myNode.get_next()
        if myNode.get_next() == None:
            newList.append(myNode.get_data())
    return newList


def get_chain_length(myNode):
    ct = 0
    while myNode.get_next() != None:
        ct += 1
        myNode = myNode.get_next()
    return ct + 1


def merge_two_chains_mine(node1, node2):
    nodelist = []
    temp1 = node1
    temp2 = node2
    while temp2 != None:
        nodelist.append(temp1)
        nodelist.append(temp2)

        temp1 = temp1.get_next()
        temp2 = temp2.get_next()

    newNode = nodelist[0]
    i = 1
    nodeCt = 1
    while nodeCt < len(nodelist):
        tempNode = nodelist[i]
        newNode.set_next(tempNode)
        newNode = newNode.get_next()
        nodeCt += 1
        i += 1
    return newNode


def merge_two_chains(node1, node2):
    nodelist = []
    temp1 = node1
    temp2 = node2
    while temp2 != None:
        nodelist.append(temp1.get_data())
        nodelist.append(temp2.get_data())
        temp1 = temp1.get_next()
        temp2 = temp2.get_next()
    head = Node(nodelist[0])
    current = head
    nodelist = nodelist[1:]
    for items in nodelist:
        current.set_next(Node(items))
        current = current.get_next()
    return head


def merge_two_chains_old(node1, node2):
    while node2 != None:
        res = Node(node1.get_data())

        while node2:
            tempNode = res
            while tempNode.get_next() != None:
                tempNode = tempNode.get_next()
            tempNode.set_next(Node(node2.get_data()))
            tempNode = res
    return res


class MyList:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def add(self, item):
        self.__items.append(item)

    def search(self, value):
        return value in self.__items

    def remove(self, value):
        self.__items.pop(self.__items.index(value))


def remove_all(list_of_values, value):
    if list_of_values.search(value) == False:
        return False
    while list_of_values.search(value):
        list_of_values.remove(value)
    return True
