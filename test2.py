def get_n_largest(my_list, n):
    if len(my_list) < n:
        num_of_nones = n - len(my_list)
        nones = [None for i in range(num_of_nones)]
        return sorted(my_list) + nones
    return sorted(my_list)[::-1][:n][::-1]


def get_adjacent_sum_dict(my_list):
    new_dict = {}
    for i in range(len(my_list) - 1):
        first = my_list[i]
        second = my_list[i+1]
        the_sum = first + second
        if the_sum not in new_dict:
            new_dict[the_sum] = [(first, second)]
        else:
            new_dict[the_sum].append((first, second))
    return new_dict


def read_temperatures(filename):
    try:
        if filename == '':
            return 'ERROR: Invalid filename!'
        file_in = open(filename, 'r')

        items = file_in.readlines()
        file_in.close()

        array_of_temp_tuples = []

        line_number = 1

        for i in range(len(items)):
            each = items[i]
            group = each.split()
            if len(group) == 1 or len(group) == 0:
                print('Invalid data at day {}'.format(line_number))
            else:
                first = float(group[0])
                second = float(group[1])
                tp = (line_number, first, second)
                array_of_temp_tuples.append(tp)
            line_number += 1
        return array_of_temp_tuples

    except FileNotFoundError:
        return "ERROR: The file '{}' does not exist.".format(filename)


class Employee:
    def __init__(self, surname, firstname, job_title, IRD_number=0, weekly_salary=0):
        self.__surname = surname
        self.__firstname = firstname
        self.__job_title = job_title
        self.__ird = IRD_number
        self.__weekly_salary = weekly_salary

    def __str__(self):
        return '{}, {}({}), title={}, weekly salary=${}'.format(self.__surname, self.__firstname, self.__ird, self.__job_title, self.__weekly_salary)

    def get_names(self):
        return '{}, {}'.format(self.__surname, self.__firstname)

    def get_job_title(self):
        return self.__job_title

    def get_IRD_number(self):
        return self.__ird

    def get_weekly_salary(self):
        return self.__weekly_salary

    def set_IRD_number(self, new_ird):
        if new_ird >= 0:
            self.__ird = new_ird

    def set_weekly_salary(self, new_salary):
        if new_salary >= 0:
            self.__weekly_salary = new_salary

    def set_job_title(self, new_job_title):
        self.__job_title = new_job_title


class Department:
    def __init__(self, department_name):
        self.__department_name = department_name
        self.__employee_list = []

    def __str__(self):
        listOfEmployees = [em.__str__() for em in self.__employee_list]
        strToReturn = self.__department_name + '\n'
        for i in range(len(listOfEmployees) - 1):
            em = listOfEmployees[i]
            strToReturn += em + '\n'
        return strToReturn + listOfEmployees[-1]

    def get_department_name(self):
        return self.__department_name

    def set_department_name(self, department_name):
        self.__department_name = department_name

    def add_employee(self, employee):
        self.__employee_list.append(employee)

    def lookup(self, employee_IRD_number):
        for em in self.__employee_list:
            if em.get_IRD_number() == employee_IRD_number:
                return em
        return 'No such Employee'

    def remove_employee(self, employee_IRD_number):
        for i in range(len(self.__employee_list)):
            em = self.__employee_list[i]
            if em.get_IRD_number() == employee_IRD_number:
                self.__employee_list.pop(i)
                return True
        return False

    def update_weekly_salary(self, employee_IRD_number, new_salary):
        em = self.lookup(employee_IRD_number)
        if em != 'No such Employee':
            em.set_weekly_salary(new_salary)
            return True
        return False


def get_positive_even_list(numbers):
    if numbers == []:
        return []
    elif numbers[0] % 2 == 0 and numbers[0] > 0:
        return [numbers[0]] + get_positive_even_list(numbers[1:])
    return get_positive_even_list(numbers[1:])


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('The stack is empty!')
        return self.__items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('The stack is empty!')
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: ' + str(self.__items)


class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('The queue is empty!')
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        if self.is_empty():
            raise IndexError('The queue is empty!')
        return self.__items[len(self.__items)-1]

    def __str__(self):
        temp = self.__items[::-1]
        return 'Queue: ' + str(temp)


class Node:
    def __init__(self, init_data, init_next=None):
        self.__data = init_data
        self.__next = init_next

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

    def __str__(self):
        return str(self.__data)

    def add_after(self, value):
        new_node = Node(value, self.__next)
        self.__next = new_node

    def remove_after(self):
        self.__next = self.__next.get_next()


def move_k_elements_to_bottom(stack, k):
    uselessStack = Stack()
    moved_stacks_b_to_top = []
    unshifted = []

    for i in range(k):
        to_move = stack.peek()
        stack.pop()
        moved_stacks_b_to_top.append(to_move)
    moved_stacks_b_to_top = moved_stacks_b_to_top[::-1]

    while stack.size() != 0:
        popped = stack.pop()
        unshifted.append(popped)
    unshifted = unshifted[::-1]

    for n in moved_stacks_b_to_top:
        stack.push(n)
    for n in unshifted:
        stack.push(n)


def interleave(q1, q2):
    newQueue = Queue()
    while q1.is_empty() == False:
        newQueue.enqueue(q1.dequeue())
    while newQueue.is_empty() == False:
        q1.enqueue(newQueue.dequeue())
        q1.enqueue(q2.dequeue())


def print_circular_node_chain(first_node):
    if first_node.get_next() == first_node:
        print(first_node.get_data())
        return

    current = first_node
    print(current.get_data())
    while current.get_next() != first_node:
        current = current.get_next()
        print(current.get_data())


def remove_duplicates(linked_list):
    existingItems = []
    curr = linked_list.get_head()
    prev = None
    while curr:
        if curr.get_data() not in existingItems:
            existingItems.append(curr.get_data())
            prev = curr
        else:
            prev.remove_after()
        curr = curr.get_next()


class LinkedList:
    def __init__(self):
        self.__head = None

    def get_head(self):
        return self.__head

    def __str__(self):
        result_list = []
        if self.__head != None:
            current = self.__head
            while current != None:
                result_list.append(str(current.get_data()))
                current = current.get_next()
        return '[' + ', '.join(result_list) + ']'

    def __iter__(self):
        return LinkedListNoDuplicatesIterator(self.__head)

    def add(self, new):
        curr = self.__head
        node = Node(new)
        if not curr:
            self.__head = node
        else:
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(node)


class LinkedListNoDuplicatesIterator:
    def __init__(self, head):
        self.__current = head
        self.__existingOnes = []

    def __next__(self):
        curr = self.__current

        while curr != None and curr.get_data() in self.__existingOnes:
            curr = curr.get_next()
        if curr == None:
            raise StopIteration

        self.__current = self.__current.get_next()
        self.__existingOnes.append(curr.get_data())
        return curr.get_data()

    def is_duplicated(self, item):
        if item not in self.__existingOnes:
            self.__existingOnes.append(item)
            return False
        return True


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

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right


class HashTable:
    def __init__(self, size):
        self.__items = size*[None]
        self.__size = size
        self.__count = 0

    def put(self, value):
        if self.__count < self.__size:
            h = value % self.__size
            while self.__items[h] != None:
                h = (h + 1) % self.__size
            self.__items[h] = value
            self.__count += 1

    def __str__(self):
        result = ''
        for i in range(self.__size):
            result = result + str(i) + ':' + str(self.__items[i]) + ' '
        return result


def worst_index(size, values):
    assert(len(values) < size)

    table = [None] * size
    for n in values:
        index = n % size
        index2 = index

        while table[index2]:
            index2 += 1
            if index2 == size:
                index2 = 0
        table[index2] = True

    ix0 = table.index(None)

    lengths = [None] * size
    ix = ix0
    length = 0
    while True:
        if table[ix]:
            length = length + 1
        else:
            length = 0
        lengths[ix] = length
        if ix == 0:
            ix = size - 1
        else:
            ix -= 1
        if ix == ix0:
            break

    max_length = max(lengths)

    worstIndices = []
    for ix in range(size):
        if lengths[ix] == max_length:
            worstIndices.append(ix)
    return worstIndices


def get_sum_internal_nodes(root):
    if root == None or (root.get_left() == None and root.get_right() == None):
        return 0

    if root.get_left() or root.get_right():
        return root.get_data() + get_sum_internal_nodes(root.get_left()) + get_sum_internal_nodes(root.get_right())


def all_paths_to_leaves(a_list):
    return []


def get_paths_largest_sum(root):
    # get all the possible paths to be searched
    all_paths = all_paths_to_leaves(root)

    # initialise the maximum sum to 0
    max_sum = 0

    # go through each last of all the paths
    for each in all_paths:
        # updating the largest sum if the current sum of the path is reater
        if sum(each) > max_sum:
            max_sum = sum(each)
    return [each for each in all_paths if sum(each) == max_sum]


def get_sum_levels_with_helper(root):
    to_return = []

    # helper function that reaches deeper of the tree using recursion
    def helper_function(root, level):
        if root is None:
            return
        if level >= len(to_return):
            to_return.append([root.get_data()])
        else:
            to_return[level].append(root.get_data())

        level += 1
        helper_function(root.get_left(), level)
        helper_function(root.get_right(), level)

    helper_function(root, 0)
    return [sum(each) for each in to_return]


def get_sum_levels(root):
    to_return = []
    curr = [root]
    while curr:
        temp = []
        val = []
        for each in curr:
            if not each:
                continue
            val.append(each.get_data())
            temp.append(each.get_left())
            temp.append(each.get_right())
        if val:
            to_return.append(val)
        curr = temp
    return [sum(each) for each in to_return]
