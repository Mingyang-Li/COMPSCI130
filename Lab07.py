'''
COMPLEXITY
'''

'''Q1'''


def rate(n):
    import math
    total = 0
    i = n
    while i > 1:
        total += i
        i = i / 2
    ops = round(3 * math.log(n, 2) + 4)
    print("Number of operations: {}".format(ops))


'''Q2'''


def rateNew(n):
    import math
    ops = 0
    total = 0
    i = 0
    ops += 2
    while i < n:
        j = 0
        ops += 3
        while j < 10:
            total = i * j + total
            j = j + 1
            ops += 3
        i = i + 1
        ops += 1
    ops += 2
    print("Number of operations: {}".format(ops))
    return total


'''Q3 and A4 needed no code'''

'''Q5'''


def compare(data, index1, index2, ct_dict):
    ct_dict[0] += 1
    return data[index1] > data[index2]


'''Q6'''


def swap(data, index1, index2, ct_dict):
    data[index1], data[index2] = data[index2], data[index1]
    ct_dict[1] += 1


'''Q7'''


def bubble_sort(data):
    n = len(data)
    count_dict = {0: 0, 1: 0}
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if compare(data, j, j+1, count_dict):
                swap(data, j, j+1, count_dict)
    print("Length: {} Comparisons: {} Swaps: {}".format(
        n, count_dict[0], count_dict[1]))


'''Q8'''


def selection_sort(data):
    count_dict = {0: 0, 1: 0}
    for fill_slot in range(len(data) - 1, 0, -1):
        pos_of_max = 0
        for i in range(1, fill_slot + 1):
            if compare(data, i, pos_of_max, count_dict):
                pos_of_max = i
        swap(data, fill_slot, pos_of_max, count_dict)
    print("Length: {} Comparisons: {} Swaps: {}".format(
        len(data), count_dict[0], count_dict[1]))


'''Q9'''


def insertion_sort(data):
    n = len(data)
    count_dict = {0: 0, 1: 0}
    """Sorts the list into ascending order"""
    for index in range(1, len(data)):
        position = index
        while position > 0 and compare(data, position - 1, position, count_dict):
            swap(data, position - 1, position, count_dict)
            position -= 1
    print("Length: {} Comparisons: {} Swaps: {}".format(
        n, count_dict[0], count_dict[1]))


'''Q10'''


def bubble_sort_fast(data):
    count_dict = {0: 0, 1: 0}
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if compare(data, i, i+1, count_dict):
                swap(data, i, i+1, count_dict)
                swapped = True
        n -= 1
    print("Length: {} Comparisons: {} Swaps: {}".format(
        len(data), count_dict[0], count_dict[1]))
