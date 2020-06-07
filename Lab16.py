def get_simple_numeric_hash(key, table_size):
    n = key ** 2
    n = int(str(n)[1:-1])
    return n % table_size


def get_simple_hash(key, table_size):
    asciiList = []
    for c in key:
        asciiList.append(ord(c))
    return sum(asciiList) % table_size


class Student:
    def __init__(self, first_name, surname, student_id, email_address):
        self.__first_name = first_name
        self.__surname = surname
        self.__student_id = student_id
        self.__email_address = email_address
        self.__test_mark = 0
        self.__exam_mark = 0
        self.__lab_marks = []

    def __str__(self):
        return '{}, {}: id={} ({})'.format(self.__surname.title(), self.__first_name.title(), self.__student_id,  self.__email_address)

    def __eq__(self, other):
        return self.__student_id == other

    def __hash__(self):
        return get_simple_hash(self.__student_id, 11)


def hash_linear(key, table):
    probeCt = 0
    i = key % len(table)

    ct = 1
    while table[i] != None:
        if i < len(table):
            i = (i+1) % len(table)
        else:
            i = 0
        ct += 1
        probeCt += 1

    probeCt += 1
    table[i] = key
    return (probeCt, table)


def hash_double(key, table):
    h1 = key % len(table)

    probeCt = 0
    index = h1
    if table[index] != None:
        while table[index] != None:
            h2 = 5 - (key % 5)
            newIndex = (h1 + probeCt * h2) % len(table)
            probeCt += 1
            index = newIndex
    else:
        probeCt += 1
    table[index] = key
    return (probeCt, table)


'''
values = [88, None, 35, 25, 10, None, None, None, None, None, 32]
probes = hash_double(11, values)
print('Table =', probes[1])
print('Probes =', probes[0])
print()

values = [None, 11, 2, 3, 4, None, 18]
probes = hash_double(9, values)
print('Table =', probes[1])
print('Probes =', probes[0])
print()


values = [0, None, None, 3, None, None, None]
probes = hash_double(6, values)
print('Table =', probes[1])
print('Probes =', probes[0])
print()


values = [None, 12, None, 3, 4, None, None, 7, None, 9, None]
probes = hash_double(5, values)
print('Table =', probes[1])
print('Probes =', probes[0])
print()

values = [22, None, 33, 25, 37, 24, None, None, None, 31, None]
probes = hash_double(39, values)
print('Table =', probes[1])
print('Probes =', probes[0])
'''


def hash_quadratic(key, table):
    h1 = key % len(table)
    probeCt = 0
    index = h1

    step = 1
    while table[index] != None:
        quaIndex = (h1 + step ** 2) % len(table)
        index = quaIndex
        probeCt += 1
        step += 1

    probeCt += 1
    table[index] = key
    return (probeCt, table)


class SimpleHashTable:
    def __init__(self, size=13):
        self.__size = size
        self.__slots = [None] * size

    def put(self, string_and_key_tuple):
        hash_value = self.get_hash_value(string_and_key_tuple)
        self.__slots[hash_value] = string_and_key_tuple

    def get_hash_value(self, string_and_key_tuple):
        key = string_and_key_tuple[1]
        return key % (self.__size)

    def __str__(self):
        return str(self.__slots)


class QuadraticHashTable:
    def __init__(self, size=13):
        self.__size = size
        self.__slots = [None] * size

    def put(self, key):
        distance = 1
        index = self.get_hash_value(key)
        i = self.get_hash_value(key)

        while self.__slots[i] != None:
            i = self.rehash(index, distance)
            distance += 1

        self.__slots[i] = key

    def get_hash_value(self, key):
        return key % self.__size

    def rehash(self, old_hash, distance):
        return (old_hash + distance * distance) % self.__size

    def __str__(self):
        return str(self.__slots)


'''
my_hash_table = QuadraticHashTable()
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(17)
print(my_hash_table)
print()


my_hash_table = QuadraticHashTable()
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(17)
my_hash_table.put(31)
my_hash_table.put(77)
print(my_hash_table)
print()

my_hash_table = QuadraticHashTable()
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(17)
my_hash_table.put(31)
my_hash_table.put(77)
my_hash_table.put(43)
my_hash_table.put(25)
print(my_hash_table)
'''


class DoubleHashTable:
    def __init__(self, size=13, q=11):
        self.__size = size
        self.__slots = [None] * size
        self.__q = q

    def put(self, key):
        hashValue = self.get_hash_value(key)
        step = 0
        newSlotNum = hashValue
        while self.__slots[newSlotNum] != None:
            step += 1
            secondHash = self.get_second_hash_value(key)
            newSlotNum = (hashValue + step * secondHash) % self.__size
        self.__slots[newSlotNum] = key

    def get_hash_value(self, key):
        return key % self.__size

    def get_second_hash_value(self, key):
        return self.__q - (key % self.__q)

    def __str__(self):
        return str(self.__slots)


'''
my_hash_table = DoubleHashTable(13, 11)
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(17)
my_hash_table.put(41)
print(my_hash_table)
print()

my_hash_table = DoubleHashTable()
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(15)
my_hash_table.put(28)
print(my_hash_table)
print()

my_hash_table = DoubleHashTable()
my_hash_table.put(26)
my_hash_table.put(54)
my_hash_table.put(94)
my_hash_table.put(15)
my_hash_table.put(13)
print(my_hash_table)
'''


class SimpleChainHashTable:
    def __init__(self, size=13):
        self.__size = size
        self.__slots = [[] for _ in range(size)]

    def get_hash_value(self, key):
        return key % self.__size

    def __str__(self):
        return str(self.__slots)

    def put(self, key):
        hashValue = self.get_hash_value(key)
        self.__slots[hashValue].append(key)

    def __len__(self):
        ct = 0
        for eachList in self.__slots:
            if eachList != []:
                for n in eachList:
                    ct += 1
        return ct


x = SimpleChainHashTable()
print("Hashtable:", x)
x.put(26)
x.put(39)
x.put(11)
x.put(17)
x.put(41)
print("Hashtable:", x)
print(len(x))

'''
myList = [[26, 39], [], [41], [], [17], [], [], [], [], [], [], [11], []]
myList[0].append(40)
print(myList[0])
'''
