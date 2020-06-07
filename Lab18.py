def running_sum_over_6(my_list):
    ct = 0
    for n in my_list:
        if ct <= 6:
            ct += n
        elif ct > 6:
            return ct
    return -1


class Rectangle:
    import math

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle: {}cm (width) x {}cm (height)'.format(self.width, self.height)

    def get_area(self):
        return round(self.width * self.height)

    def set_height(self, data):
        self.height = data

    def set_width(self, data):
        self.width = data

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class Cipher:

    def __init__(self, offset, reverse):
        self.offset = offset
        self.reverse = reverse

    def encode(self, message):
        new_msg = ''
        for i in range(len(message)):
            n = ord(message[i])
            n += self.offset

            if n < 97:
                n += 26
            elif n > 122:
                n -= 26

            char = chr(n)
            new_msg += char
        if self.reverse:
            return new_msg[::-1]
        return new_msg

    def decode(self, encrypted):
        if self.reverse:
            encrypted = encrypted[::-1]

        message = ''
        for i in range(len(encrypted)):
            n = ord(encrypted[i])
            n -= self.offset

            if n < 97:
                n += 26
            elif n > 122:
                n -= 26

            char = chr(n)
            message += char
        return message.lower()


class StackNormal:
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
        return 'Stack: {} <- top of the stack'.format(str(self.__items))

    def slice(self, start, stop, step=1):
        new_stack = Stack()
        if self.is_empty():
            return new_stack
        else:
            new_slice = [self.__items[i] for i in range(start, stop, step)]
            for n in new_slice:
                new_stack.push(n)
            return new_stack


class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[self.size() - 1]

    def __str__(self):
        return 'Queue: front->{}<- end'.format(str(self.__items[::-1]))

    def splice(self, second_queue):
        for i in range(second_queue.size()-1, -1, -1):
            item = second_queue.__items[i]
            self.enqueue(item)


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


def create_chain(elements):
    if elements == []:
        return None
    i = 1
    head = Node(elements[0])
    current = head
    while i <= len(elements) - 1:
        the_next = Node(elements[i])
        current.set_next(the_next)
        current = current.get_next()
        i += 1
    return head


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
        result = "["
        separator = ""
        current = self.__head
        while current != None:
            result += separator + str(current.get_data())
            separator = ", "
            current = current.get_next()
        result += "]"
        return result

    def has_same_elements(self, second_linked_list):
        if self.is_empty() and second_linked_list.is_empty():
            return True

        elif (self.is_empty() and second_linked_list.is_empty() == False):
            return False
        elif (self.is_empty() == False and second_linked_list.is_empty()):
            return False

        curr1 = self.__head
        curr2 = second_linked_list.__head

        curr1_items = []
        curr2_items = []

        while curr1 and curr2:

            curr1_data = curr1.get_data()
            curr1_items.append(curr1_data)
            curr1 = curr1.get_next()

            curr2_data = curr2.get_data()
            curr2_items.append(curr2_data)
            curr2 = curr2.get_next()

        equal = list(set(curr1_items)) == list(set(curr2_items))
        if equal == False:
            return False

        return True


class Stack:
    def __init__(self):
        self.__head = None

    def __str__(self):
        return str(self.__head)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        if self.__head == None:
            self.__head = Node(item)
        else:
            curr = self.__head
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(Node(item))

    def pop(self):
        if self.__head == None:
            return None
        if self.__head.get_next() == None:
            curr = self.__head
            self.__head = None
            return curr
        curr = self.__head
        while curr.get_next().get_next() != None:
            curr = curr.get_next()

        popped = curr.get_next()
        '''
        print('curr is', curr.get_data())
        print('before popping, the next of curr is', curr.get_next().get_data())
        '''
        curr.set_next(None)
        return popped

    def peek(self):
        curr = self.__head
        while curr.get_next():
            curr = curr.get_next()
        return curr

    def size(self):
        if self.__head == None:
            return 0
        ct = 0
        curr = self.__head
        while curr:
            curr = curr.get_next()
            ct += 1
        return ct


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.__left)
            self.__left = t

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.__right)
            self.__right = t

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_left(self, le):
        self.__left = le

    def set_right(self, ri):
        self.__right = ri


def get_rightmost_data(b_tree):
    curr_right_most = b_tree.get_right()
    if curr_right_most == None:
        return b_tree.get_data()
    while curr_right_most.get_right():
        curr_right_most = curr_right_most.get_right()
    return curr_right_most.get_data()


def print_leaf_nodes(root):
    if root == None:
        return
    if root.get_left() == None and root.get_right() == None:
        print(root.get_data(), end=' ')
    if root.get_left():
        print_leaf_nodes(root.get_left())
    if root.get_right():
        print_leaf_nodes(root.get_right())


class Folder:
    def __init__(self, folder_name, list_of_subfolders, list_of_filenames):
        self.__name = folder_name
        self.__subfolders = list_of_subfolders
        self.__files = list_of_filenames

    def __str__(self):
        return self.__name

    def get_files(self):
        return self.__files

    def get_subfolders(self):
        return self.__subfolders


def folder_search(folder, file):
    if file in folder.get_files():
        return folder

    subfolders = folder.get_subfolders()
    for i in range(len(subfolders)):
        currFolder = subfolders[i]
        if file in currFolder.get_files():
            return currFolder
        else:
            return folder_search(currFolder, file)


def folder_search_not_working(folder, file):
    if file in folder.get_files():
        return folder

    subfolders = folder.get_subfolders()
    for i in range(len(subfolders)):

        currSubFolder = folder.get_subfolders()[i]
        if file in currSubFolder.get_files():
            return currSubFolder
        else:
            newSubfolders = subfolders[i:]
            list_of_file_names = folder.get_files()
            newFolder = Folder(folder, newSubfolders, list_of_file_names)
            return folder_search(newFolder, file)


b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
c = Folder('Folder_c', [], ['File_3', 'File_4'])
a = Folder('Folder_a', [b, c], [])
print(folder_search(a, 'File_3'))
print()

b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
c = Folder('Folder_c', [], ['File_3', 'File_4'])
a = Folder('Folder_a', [b, c], ['File_5', 'File_6'])
print(folder_search(a, 'File_0'))
print()

b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
c = Folder('Folder_c', [], ['File_3', 'File_4'])
a = Folder('Folder_a', [b, c], ['File_5', 'File_6'])
print(folder_search(a, 'File_5'))
print()

a = Folder('Folder_a', [], ['File_0', 'File_1'])
print(folder_search(a, 'File_that_does_not_exist'))
print()


d = Folder('Folder_d', [], ['File_7'])
e = Folder('Folder_e', [], [])
b = Folder('Folder_b', [], ['File_0', 'File_1', 'File_2'])
c = Folder('Folder_c', [d, e], ['File_3', 'File_4'])
a = Folder('Folder_a', [b, c], ['File_5', 'File_6'])
print(folder_search(a, 'File_7'))
print()


a = Folder('Folder_a', [], ['File_0', 'File_1'])
result = folder_search(a, 'File_1')
if not isinstance(result, Folder):
    print('The folder_search function must return a Folder object')
print(folder_search(a, 'File_1'))
