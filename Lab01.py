'''Q1'''
filename = input("Enter a filename: ")
file_in = open(filename, "r")
content = file_in.readlines()
file_in.close()
even_ct = 0
odd_ct = 0

for line in content:
    if len(line) != 1:
        num_arr = [int(i) for i in line.split()]
        for c in num_arr:
            if int(c) % 2 == 0:
                even_ct += 1
            else:
                odd_ct += 1

print("There are {} even number(s) and {} odd number(s).".format(even_ct, odd_ct))

'''Q2'''


def test1(f):
    opened = open(f)
    body = opened.read()
    opened.close()
    a_list = body.split()
    sorted_list = sorted(a_list, key=len)
    word = sorted_list[-1]

    reduced = filter(lambda x: len(x) == len(sorted_list[-1]), sorted_list)
    return "The longest word is \"" + sorted(list(reduced))[-1] + "\""


print(test1(input("Enter filename: ")))


def get_sum_negative_odd(num_arr):
    sum = 0
    if len(num_arr) == 0:
        return 0
    for n in num_arr:
        if n < 0 and abs(n) % 2 == 1:
            sum += n
    return sum


'''Q3'''


def repeats_exist(num_arr):
    if len(num_arr) == len(set(num_arr)):
        return False
    else:
        return True


'''Q4'''


def get_multiples_of_3(num_arr):
    return list(filter(lambda x: x % 3 == 0, num_arr))


'''Q5'''


def count_vowels(word):
    vowel = "aeiouAEIOU"
    return len(list(n for n in word if n in vowel))


'''Q6'''
filename = str(input("Enter the English to French dictionary filename: "))
file_in = open(filename, "r")
content = file_in.readlines()
lang_dict = {}
for i in range(0, len(content), 1):
    pair = content[i]
    mid_index = pair.find(":")
    if i < (len(content)-1):
        newline_ch_i = pair.find("\n")
        key = pair[:mid_index]
        value = pair[mid_index+1:newline_ch_i]
        lang_dict[str(key)] = str(value)
    elif i == (len(content)-1):
        key = pair[:mid_index]
        value = pair[mid_index+1:]
        lang_dict[str(key)] = str(value)
file_in.close()
eng_word = input("Enter a English word: ")

'''Q7'''
matched = False
for wd in lang_dict:
    if eng_word == wd:
        french = lang_dict[wd]
        print("'{}' is translated into '{}'.".format(wd, french))
        matched = True

if matched == False:
    print("Sorry that word doesn't exist in French!")

'''Q8'''


def print_reverse_keys(a_dict):
    keys = sorted(a_dict.keys())
    for i in range(len(keys)-1, -1, -1):
        print(keys[i], a_dict[keys[i]])


'''Q9'''


def print_keys_values_inorder(a_dict):
    key_list = sorted(a_dict.keys())
    for key in key_list:
        value_list = sorted(a_dict[key])
        v = " ".join(value_list)

        print("{} {}".format(key, v))


'''Q10'''
sentence = input("Enter a sentence: ")
sentence = str(sentence)
wd_list = sentence.split()
new_dict = {}
for w in wd_list:
    w = w.lower()
    if w not in new_dict:
        new_dict[w] = 0
    if w in new_dict:
        new_dict[w] += 1

key_list = sorted(new_dict.keys())
for k in key_list:
    print(str(k) + ":" + str(new_dict[k]))
