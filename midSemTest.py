'''q1'''

'''
def create_string_len_tuple(myList):
    return [(item, len(item) for item in myList)]
'''

'''q2'''
rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))
'''
spaces = rows - 1
for r in rows:
    print('*' * spaces + '*' * cols)
    spaces -= 1
'''

'''q3'''


def create_surnames_dictionary(nameList):
    newDict = {}
    for fullName in nameList:
        key = fullName[fullName.find(' ') + 1]
        if key not in newDict:
            newDict[key] = [fullName]

        else:
            newDict[key].append(fullName)
        newDict[key] = sorted(newDict[key])
    return newDict


'''q4'''
filename = input('Enter a filename: ')
file_in = open(filename, 'r')
content = file_in.read()
file_in.close()
fullNames = content.split()
nameArr = []
for name in fullNames:
    first = name[name.find(',')+1:]
    last = name[:name.find(',')]
    nameArr.append('{} {}'.format(first, last))
print(nameArr)

'''q5'''
filename = input('Enter a filename: ')
try:
    file_in = open(filename, 'r')
    content = file_in.read()
    file_in.close()
    fullNames = content.split()
    nameArr = []
    fullNames = filter(lambda x: ',' in x, fullNames)
    for name in fullNames:
        first = name[name.find(',')+1:]
        last = name[:name.find(',')]
        nameArr.append('{} {}'.format(first, last))
    print(nameArr)
except FileNotFoundError:
    print("ERROR: The file '{}' does not exist.".format(filename))


'''q6'''


def rate(n):
    ct = 0
    total = 0
    i = 1
    ct += 2
    while i < n:
        j = 0
        ct += 2
        while j < n:
            total = i * j + total
            j = j + 1
            ct += 3
        i = i * 2
        ct += 2
    ct += 2
    print('Number of operations: ' + str(ct))
    return total


'''q7, q8'''


class MyTriangle:
    def __init__(self, side_a=1.0, side_b=1.0, side_c=1.4):
        self.__side_a = float(side_a)
        self.__side_b = float(side_b)
        self.__side_c = float(side_c)

    def get_side_a(self):
        return float(self.__side_a)

    def get_side_b(self):
        return float(self.__side_b)

    def get_side_c(self):
        return float(self.__side_c)

    def set_side_a(self, newside_a):
        if newside_a > 0:
            self.__side_a = newside_a

    def set_side_b(self, newside_b):
        if newside_b > 0:
            self.__side_b = newside_b

    def set_side_c(self, newside_c):
        if newside_c > 0:
            self.__side_c = newside_c

    def __str__(self):
        return 'The sides of a triangle are: {}, {}, {}.'.format(round(self.__side_a, 1), round(self.__side_b, 1), round(self.__side_c, 1))

    def get_perimeter(self):
        return round(sum([self.__side_a, self.__side_b, self.__side_c]), 2)

    def get_area(self):
        import math
        s = sum([self.__side_a, self.__side_b, self.__side_c]) / 2
        area = math.sqrt(s * (s - self.__side_a) *
                         (s - self.__side_b) * (s - self.__side_c))
        return round(area, 2)

    def is_valid(self):
        return (self.__side_a + self.__side_b) > self.__side_c and (self.__side_a + self.__side_c) > self.__side_b and (self.__side_c + self.__side_b) > self.__side_a


'''q9'''


class Rugby:
    def __init__(self, country_name='N/A', rugby_points=0):
        self.__country_name = country_name
        self.__rugby_points = rugby_points

    def __str__(self):
        return 'Country: {}({})'.format(self.__country_name, self.__rugby_points)

    def get_country_name(self):
        return self.__country_name

    def get_points(self):
        return self.__rugby_points


'''q10'''


def read_rugby_list(filename):
    try:
        file_in = open(filename, 'r')
        content = file_in.read()
        file_in.close()
        content = content.split("\n")
        return [Rugby(item[:item.find(',')], int(item[item.find(',')+1:])) for item in content]
    except FileNotFoundError:
        print("ERROR: The file '{}' does not exist.".format(filename))
        return ''


'''q11'''


def selection_sort(data):
    for pass_num in range(len(data) - 1, 0, -1):
        position_largest = 0
        for i in range(1, pass_num+1):
            if data[i].get_points() > data[position_largest].get_points():
                position_largest = i
            elif data[i].get_points() == data[position_largest].get_points():
                if data[i].get_country_name() > data[position_largest].get_country_name():
                    position_largest = i
                else:
                    position_largest = position_largest

        data[position_largest], data[i] = data[i], data[position_largest]


'''q12'''


def check_binary_search(sorted_rugby_list, search_country_name):
    if search_country_name not in [item.get_country_name() for item in sorted_rugby_list]:
        return -1
    high = len(sorted_rugby_list)-1
    low = 0
    ct = 0
    while low <= high:
        mid = (high + low) // 2
        if sorted_rugby_list[mid].get_country_name() == search_country_name:
            return ct+1
        elif sorted_rugby_list[mid].get_country_name() < search_country_name:
            low = mid + 1
        else:
            high = mid - 1
        ct += 1
    return ct


'''q13'''


def binary_search_tuples(tpList, targetTp):
    if len(tpList) == 0:
        return (-1, 0)
    if len(tpList) == 1:
        if tpList[0] == targetTp:
            return (0, 1)
        else:
            return (-1, 1)
    low = 0
    high = len(tpList) - 1
    step = 0
    while low <= high:
        step += 1
        mid = (low + high) // 2
        if tpList[mid] < targetTp:
            low = mid + 1
        else:
            if tpList[mid] == targetTp:
                return (mid, step)
            else:
                high = mid - 1
    return (-1, step)


'''q14'''


def trinary_search(my_list, x):
    if len(my_list) == 1:
        if x == my_list[0]:
            return (0, [0])
        else:
            return (-1, [0, 0])

    left = 0
    right = len(my_list) - 1
    list_of_mid_points = []

    while right >= left:

        mid1 = left + (right - left) // 3
        list_of_mid_points.append(mid1)

        if x == my_list[mid1]:
            return (mid1, list_of_mid_points)

        if x < my_list[mid1]:
            right = mid1 - 1

        else:
            mid2 = right - (right - left) // 3
            list_of_mid_points.append(mid2)

            if x == my_list[mid2]:
                return (mid2, list_of_mid_points)
            else:
                if x > my_list[mid2]:
                    left = mid2 + 1
                else:
                    left = mid1 + 1
                    right = mid2 - 1
    return (-1, list_of_mid_points)


'''q15'''


def find_k_smallest_elements(data, k):
    num_comparisons = 0
    num_swaps = 0
    for pass_num in range(len(data) - 1, max(len(data)-1 - k, 0), -1):
        position_smallest = 0
        for i in range(1, pass_num+1):
            num_comparisons += 1
            if data[i] < data[position_smallest]:
                position_smallest = i
        data[position_smallest], data[pass_num] = data[pass_num], data[position_smallest]
        num_swaps += 1
    return (data[-k:], num_comparisons, num_swaps)


'''q16'''


def bubble_sort(my_list):
    n = len(my_list)
    newList = my_list.copy()
    num_comparisons = num_swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            num_comparisons += 1
            if newList[j] > newList[j+1]:
                num_swaps += 1
                newList[j], newList[j+1] = newList[j+1], newList[j]
    return (num_comparisons, num_swaps)


def split_list(my_list, section_size):
    for i in range(0, len(my_list), section_size):
        yield my_list[i:i + section_size]


def bubble_section_sort(my_list, section_size):
    print(my_list)
    print(bubble_sort(my_list))
    listOfLists = list(split_list(my_list, section_size))

    listOfAverage = [round(sum(item) / len(item), 1) for item in listOfLists]

    item_average_dict = {}
    i = 0
    for avg in listOfAverage:
        item_average_dict[avg] = listOfLists[i]
        i += 1
    sortedListOfAverage = sorted(listOfAverage)
    sortedListOfList = []
    for av in sortedListOfAverage:
        sortedListOfList.append(item_average_dict[av])

    mergedList = []
    for item in sortedListOfList:
        for n in item:
            mergedList.append(n)
    print(mergedList)
    print(bubble_sort(mergedList))

