'''q1-q5'''


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return 'Stack: ' + str(self.__items)

    def multi_push(self, element, how_many):
        for i in range(how_many):
            i = i
            self.__items.append(element)

    def to_list(self):
        newList = []
        for n in self.__items:
            newList.append(n)
        return newList

    def slice(self, start=0, stop=-1, step=1):
        newList = []
        for i in range(start, stop, step):
            newList.append(self.__items[i])
        return 'Stack: {}'.format(newList)

    def reverse(self):
        self.__items.reverse()


'''q6'''


def countup_stack(number):
    newStack = Stack()
    i = 1
    while i <= number:
        newStack.push(i)
        i += 1
    return newStack


'''q7'''
postfix_stack = Stack()
postfix_stack.push(3)
postfix_stack.push(4)

last1 = postfix_stack.pop()
last2 = postfix_stack.pop()
postfix_stack.push(last1 * last2)


postfix_stack.push(6)


last1 = postfix_stack.pop()
last2 = postfix_stack.pop()
postfix_stack.push(last2 / last1)


postfix_stack.push(3)

last1 = postfix_stack.pop()
last2 = postfix_stack.pop()
postfix_stack.push(last2 + last1)

print(postfix_stack.peek())

'''q8'''


def compute(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 // number2
    else:
        return number1 ** number2


def evaluate_postfix(myList):
    newStack = Stack()
    for n in myList:
        if n.isdigit():
            newStack.push(int(n))
        else:
            symbol = n
            last1 = newStack.pop()
            last2 = newStack.pop()
            newStack.push(compute(last2, last1, symbol))
    return newStack.peek()


'''q9'''


def read_reverse_integers(num):
    ct = 0
    newStack = Stack()
    while ct < num:
        userInput = int(input('Enter an integer: '))
        newStack.push(userInput)
        ct += 1
    toPrint = []
    for i in range(newStack.size()):
        i = i
        if newStack.peek() not in toPrint:
            last = newStack.pop()
            toPrint.append(last)
        elif newStack.peek() in toPrint and newStack.peek() != toPrint[-1]:
            last = newStack.pop()
            toPrint.append(last)
        else:
            newStack.pop()
    for n in toPrint:
        print(n)


'''q10'''


def get_longest_run(string):
    n = len(string)
    stk = []
    stk.append(-1)
    result = 0

    for i in range(n):

        if string[i] == '(':
            stk.append(i)

        else:
            stk.pop()
            if len(stk) != 0:
                result = max(result, i - stk[len(stk)-1])
            else:
                stk.append(i)
    return result
