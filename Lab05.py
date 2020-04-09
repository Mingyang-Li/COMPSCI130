'''
DEBUGGING
'''

'''Q1'''


def remove_letters(word1, word2):
    result = list(word2)
    for letter in word1:
        if letter in result:
            result.remove(letter)
    return ''.join(result)


'''Q2'''


def print_hollow(number_of_rows, number_of_columns):
    if number_of_rows > 1 and number_of_columns > 1:
        print('*' * number_of_columns)
        for row in range(number_of_rows-2):
            print('*' + ' ' * (number_of_columns-2) + '*')
        print('*' * number_of_columns)


'''Q3'''


def get_largest(list_of_strings):
    largest = -9999
    for item in list_of_strings:
        value = float(item)
        if value > largest:
            largest = value
    return largest


'''Q4'''


def get_index_of_smallest(numbers):
    if len(numbers) == 0:
        return -1
    else:
        min_value = numbers[0]
        for num in numbers:
            if num < min_value:
                min_value = num
        return numbers.index(min_value)


'''Q5'''


def multiply(numbers, factor):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * factor


'''Q6'''


def is_adjacent(numbers):
    if len(numbers) == 1:
        return False
    elif len(numbers) == 2:
        return numbers[0] == numbers[1]
    else:
        for i in range(0, len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                return True
        return False


'''Q7'''


def tuple_append(my_tuple, number):
    return (my_tuple[0], my_tuple[1], number)


'''Q8'''


def append_to(element, values=None):
    if values == None:
        return [element]
    else:
        values.append(element)
        return values


'''Q9'''


def print_values(dictionary):
    for key in sorted(list(dictionary.keys())):
        print(dictionary[key], end=" ")


'''Q10'''


def create_alphabets_dictionary(names_list):
    dictionary = {}
    for name in names_list:
        first_letter = name[0]
        if first_letter not in dictionary:
            dictionary[first_letter] = [name]
        else:
            dictionary[first_letter].append(name)
    return dictionary
