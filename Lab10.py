'''Q1'''


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name


def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        j = i
        while j > 0 and list_to_sort[j-1].name < list_to_sort[j].name:
            temp = list_to_sort[j]
            list_to_sort[j] = list_to_sort[j-1]
            list_to_sort[j-1] = temp
            j -= 1


'''Q2'''


def double(my_list):
    for i in range(len(my_list)):
        my_list[i] *= 2


'''Q3'''


def get_middle_number(nums):
    if nums == sorted(nums):
        return nums[len(nums) // 2]
    else:
        return sorted(nums)[len(nums) // 2]


'''Q4'''


def get_middle_number_from_file(filename):
    file_in = open(filename, 'r')
    content = file_in.read()
    file_in.close()
    contentArr = content.split()
    contentArr = sorted([int(n) for n in contentArr])
    return contentArr[len(contentArr) // 2]


'''Q5'''
