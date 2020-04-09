'''
SORTING
'''

'''Q1, Q2 didn't require any code'''

'''Q3'''


def bubble_row(data, index):
    for i in range(index):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
    return data


'''Q4'''


def my_bubble_sort(a_list):
    for i in range(0, len(a_list)-1):
        for j in range(0, len(a_list) - 1 - i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list


'''Q5 AND Q6 NEEDS NO CODE'''

'''Q7'''


def get_largest_position(data, index):
    myList = data[:index+1]
    return data.index(max(myList))


'''Q8'''


def selection_row(data, index):
    largest = get_largest_position(data, index)
    largest_value = data[largest]
    data[largest], data[index] = data[index], largest_value


'''Q9'''


def my_selection_sort(data):
    for i in range(len(data) - 1, 0, -1):
        selection_row(data, i)


'''Q10, Q11 NEEDS NO CODE'''

'''Q12'''


def shifting(data, index):
    target = data[index]
    i = index - 1
    while i >= 0 and data[i] > target:
        data[i+1] = data[i]
        i -= 1


'''Q13'''


def insertion_row(data, index):
    target = data[index]
    i = index - 1
    while i >= 0 and target < data[i]:
        data[i+1] = data[i]
        data[i] = target
        i -= 1


'''Q14'''


def my_insertion_sort(a_list):
    for index in range(1, len(a_list)):
        target = a_list[index]
        i = index - 1
        while i >= 0 and a_list[i] > target:
            a_list[i+1] = a_list[i]
            a_list[i] = target
            i -= 1
    return a_list


'''Q15'''


def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while (min_index <= max_index):
        mid = (max_index + min_index) // 2
        if numbers[mid] < value:
            min_index = mid + 1
        elif numbers[mid] > value:
            max_index = mid - 1
        else:
            return mid
    return -1
