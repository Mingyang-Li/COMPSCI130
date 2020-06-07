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


def create_a_tree():
    root = BinaryTree(7)
    root.insert_left(2)
    root.insert_right(9)

    left = root.get_left()
    right = root.get_right()

    left.insert_left(1)
    left.insert_right(5)

    right.insert_right(14)

    return root


def create_a_bigger_tree():
    root = BinaryTree('a')

    left = BinaryTree('b')
    right = BinaryTree('c')

    root.set_left(left)
    root.set_right(right)

    newLeft = root.get_left()

    newLeft.insert_left('d')
    newLeft.insert_right('e')

    lastLeft = newLeft.get_left()
    lastRight = newLeft.get_right()

    lastLeft.insert_right('f')
    lastRight.insert_right('g')

    return root


def basic_print(bTree):
    if bTree == None:
        return
    print(bTree.get_data(), end=' ')
    basic_print(bTree.get_left())
    basic_print(bTree.get_right())


def count_nodes(root):
    if root == None:
        return 0
    return count_nodes(root.get_left()) + count_nodes(root.get_right()) + 1


def get_sum(root):
    if root == None:
        return 0
    return get_sum(root.get_left()) + get_sum(root.get_right()) + root.get_data()


def get_tree_depth(root):
    if root == None or root.get_left() == None and root.get_right() == None:
        return 0
    leftLen = get_tree_depth(root.get_left())
    rightLen = get_tree_depth(root.get_right())
    return max(leftLen, rightLen) + 1


def get_sum_leaf_nodes(root):
    if root == None:
        return 0
    elif root.get_left() == None and root.get_right() == None:
        return root.get_data()
    elif root.get_left() != None or root.get_right() != None:
        return get_sum_leaf_nodes(root.get_left()) + get_sum_leaf_nodes(root.get_right())


def no_odds(root):
    return (root == None) or ((root.get_data() % 2 == 0) and no_odds(root.get_left()) and no_odds(root.get_right()))


def convert_tree_to_list(root):
    if root == None:
        return None

    return [root.get_data(), convert_tree_to_list(root.get_left()), convert_tree_to_list(root.get_right())]


def search(root, item):
    if root == None:
        return False
    elif root.get_data() == item:
        return True
    elif search(root.get_left(), item):
        return True
    else:
        return search(root.get_right(), item)
