class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, left=self.__left)
            self.__left = t

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, right=self.__right)
            self.__right = t

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def search(self, value):
        if self.get_data() == value:
            return True
        elif value < self.get_data() and self.get_left():
            return self.get_left().search(value)
        elif value > self.get_data() and self.get_right():
            return self.get_right().search(value)
        else:
            return False

    def insert(self, value):
        if value == self.get_data():
            return

        elif value < self.get_data():
            if self.get_left() == None:
                self.set_left(BinarySearchTree(value))
            else:
                self.get_left().insert(value)
        else:
            if self.get_right() == None:
                self.set_right(BinarySearchTree(value))
            else:
                self.get_right().insert(value)


def create_bigger_bs_tree():
    root = BinarySearchTree(27)

    left = BinarySearchTree(14)
    leftLeft = BinarySearchTree(10)
    leftRight = BinarySearchTree(19)

    right = BinarySearchTree(35)
    rightLeft = BinarySearchTree(31)
    rightRight = BinarySearchTree(42)

    root.set_left(left)
    root.set_right(right)

    left.set_left(leftLeft)
    left.set_right(leftRight)

    right.set_left(rightLeft)
    right.set_right(rightRight)

    return root


def traverse_bst_inorder(root):
    if root == None:
        return

    traverse_bst_inorder(root.get_left())
    print(root.get_data(), end=' ')
    traverse_bst_inorder(root.get_right())


def traverse_bst_preorder(root):
    if root == None:
        return
    print(root.get_data(), end=' ')
    traverse_bst_preorder(root.get_left())
    traverse_bst_preorder(root.get_right())


def get_maximum(root):
    largest = root.get_data()

    if root.get_left():
        leftMax = get_maximum(root.get_left())
        largest = max(largest, leftMax)

    if root.get_right():
        rightMax = get_maximum(root.get_right())
        largest = max(largest, rightMax)

    return largest


def get_minimum(root):
    smallest = root.get_data()

    if root.get_left():
        leftMin = get_minimum(root.get_left())
        smallest = min(smallest, leftMin)

    if root.get_right():
        rightMin = get_minimum(root.get_right())
        smallest = min(smallest, rightMin)

    return smallest


def convert_to_list(root, theList):
    if root == None:
        return theList
    return convert_to_list(root.get_left(), theList) + [root.get_data()] + convert_to_list(root.get_right(), theList)


def traverse_bst_postorder(root):
    if root:
        traverse_bst_postorder(root.get_left())
        traverse_bst_postorder(root.get_right())
        print(root.get_data(), end=' ')


def create_from_list(values):
    if len(values) == 0:
        return None

    if len(values) == 1:
        return BinarySearchTree(values[0], None, None)

    mid = len(values) // 2
    return BinarySearchTree(
        values[mid],
        create_from_list(values[:mid]),
        create_from_list(values[mid+1:])
    )


def print_insert_position_old(root, num):
    if root and root.search(num):
        print('Duplicate')
        return None

    # num smaller than root
    if root and root.get_data() > num:
        # if root is leaf node, print
        if not root.get_left() and not root.get_right():
            print('To the left of', root.get_data())
            return None

        else:

            print_insert_position(root.get_right(), num)
            print_insert_position(root.get_left(), num)

    # num bigger than root
    elif root and root.get_data() < num:
        # if root is leaf node, print
        if not root.get_left() and not root.get_right():
            print('To the right of', root.get_data())
            return None
        else:
            print_insert_position(root.get_right(), num)
            print_insert_position(root.get_left(), num)


def print_insert_position(root, num):
    if root.get_data() == num:
        print('Duplicate')
        return

    elif root.get_data() < num:
        if root.get_right() == None:
            print('To the right of', root.get_data())
            return
        else:
            return print_insert_position(root.get_right(), num)

    else:
        if root.get_left() == None:
            print('To the left of', root.get_data())
            return None
        else:
            return print_insert_position(root.get_left(), num)
