def count_up(n):
    if n == 0:
        print('Go!')

    elif n > 0:
        count_up(n - 1)
        print('n went down by 1')
        print(n)


def count_down(n):
    if n > 0:

        print(n)
        count_down(n - 1)
    else:
        print('Go!')


def count_odd_list(numList):
    if len(numList) == 1:
        if numList[0] % 2 == 1:
            return 1
        else:
            return 0

    if numList[0] % 2 == 1:
        return 1 + count_odd_list(numList[1:])
    else:
        return 0 + count_odd_list(numList[1:])


def evaluate_m2(i):
    if i == 0:
        return 0
    return i / (2 * i + 1) + evaluate_m2(i-1)


def get_sum_odd_list(myList):
    if len(myList) == 0:
        return 0
    else:
        if myList[0] % 2 == 1:
            return myList[0] + get_sum_odd_list(myList[1:])
        else:
            return 0 + get_sum_odd_list(myList[1:])


def get_sum_multiple_list(myList, target):
    if len(myList) == 0:
        return 0
    else:
        if myList[0] % target == 0:
            return myList[0] + get_sum_multiple_list(myList[1:], target)
        else:
            return 0 + get_sum_multiple_list(myList[1:], target)


def get_even_list(myList):
    if len(myList) == 0:
        return []
    else:
        if myList[0] % 2 == 1:
            return get_even_list(myList[1:])
        else:
            return [myList[0]] + get_even_list(myList[1:])


def no_odds(numList):
    if len(numList) == 1:
        if numList[0] % 2 == 1:
            return False
        else:
            return True
    else:
        if numList[0] % 2 == 1:
            return False
        else:
            return no_odds(numList[1:])


def binary_search(myList, target):
    low = 0
    high = len(myList) - 1
    if low > high:
        return False

    else:
        mid = len(myList) // 2
        print(myList[:mid], myList[mid], myList[mid+1:])
        if myList[mid] < target:
            return binary_search(myList[mid+1:], target)
        elif myList[mid] > target:
            return binary_search(myList[:mid], target)
        else:
            return True
        return False
