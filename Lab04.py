'''Q1'''


def is_old_enough(age):
    try:
        if age >= 16:
            return True
        elif (0 < age < 16) or age == -1:
            raise ValueError()

    except (TypeError, ValueError):
        return "ERROR: Invalid age!"
    else:
        return False


'''Q2'''


def is_valid_score(s):
    try:
        if s >= 0 and s <= 100:
            return True
        elif (s < 0 or s > 100):
            raise()
    except:
        return "ERROR: Invalid score!"


'''Q3'''


def get_valid_input():
    number = -1  # default
    while not 1 <= number <= 10:
        try:
            user_input = input("Enter a number between 1 and 10 inclusive: ")
            number = float(user_input)
        except:
            pass
    return number


'''Q4'''


def count_vowels(myStr):
    vowel = "aeiou"
    ct = 0
    try:
        if type(myStr) is str:
            myStr = myStr.lower()
            for c in myStr:
                if c in vowel:
                    ct += 1
            return ct
        else:
            raise TypeError()
    except(TypeError, ValueError):
        return "ERROR: Invalid input!"


'''Q5'''


def get_min(numbers):
    try:
        smallest = numbers[0]
        for item in numbers:
            if type(item) is str:
                raise TypeError()
            elif item < smallest:
                smallest = item
        return float(smallest)
    except TypeError:
        return "ERROR: Invalid number!"


'''Q6'''


def get_sum(numbers):
    total = 0
    for n in numbers:
        try:
            total += n
        except TypeError:
            pass
    return total


'''Q7'''


def get_diff(aList, i1, i2):
    try:
        return aList[i1] - aList[i2]
    except IndexError:
        return "ERROR: Out of range!"
    except TypeError:
        return "ERROR: Invalid number!"


'''Q8'''


def get_french_word(myDict, word):
    try:
        return myDict[word]
    except KeyError:
        return "ERROR: {} is not available.".format(word)


'''Q9'''


def get_room(myDict, courseNum):
    try:
        if courseNum == "":
            raise ValueError()
        return myDict[courseNum]
    except KeyError:
        return "ERROR: {} is not available.".format(courseNum)
    except ValueError:
        return "ERROR: Invalid course number!"


'''Q10'''


def count_words(filename):
    try:
        if filename == "":
            return "ERROR: Invalid filename!"
        input_file = open(filename, "r")
        words = input_file.read().split()
        input_file.close()
        return len(words)
    except FileNotFoundError:
        return "ERROR: The file '{}' does not exist.".format(filename)


'''Q11'''


def get_largest(filename):
    try:
        input_file = open(filename, 'r')
        lines = input_file.readlines()
        input_file.close()
        largest = -9999
        for line in lines:
            items_list = line.split()
            for element in items_list:
                try:
                    value = float(element)
                    if value > largest:
                        largest = value
                except ValueError:
                    pass
        return largest
    except FileNotFoundError:
        return "ERROR: The file '{}' does not exist.".format(filename)
