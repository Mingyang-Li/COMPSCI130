'''Q1'''


def get_tag_words(myLine):
    i = myLine.find(":")
    return (myLine[:i], sorted(line[i+1:].split()))


'''Q2'''


def read_content(filename):
    file_in = open(filename, "r")
    content = file_in.read()
    file_in.close()
    return [item for item in content.split("\n") if len(item) > 1]


'''Q3'''


def create_tags_dictionary(filename):
    file_in = open(filename, "r")
    content = file_in.read()
    file_in.close()
    my_dict = {}
    for item in content.split("\n"):
        i = item.find(":")
        if len(item) > 1:
            my_dict[item[:i]] = sorted(item[i+1:].split(" "))
    return my_dict


'''Q4'''


def get_sorted_unique_words_list(my_str):
    return sorted(set(my_str.lower().split(" ")))


'''Q5'''


def get_word_tag_tuple(tags_dict, word):
    for key in tags_dict:
        if word in tags_dict[key]:
            return (word, key)


'''Q6'''


def get_tag_tuple_list(tag_dict, sentence):
    word_list = sorted(set(sentence.lower().split(" ")))
    list_of_tp = []
    for word in word_list:
        for key in tag_dict:
            if word in tag_dict[key]:
                list_of_tp.append((word, key))
    return list_of_tp


'''Q7'''


def filtering(my_tp, tags):
    new_arr = []
    for item in my_tp:
        if item[1] in filter:
            new_arr.append((item))
    return new_arr


'''Q8'''


def grouping(tp_list, new_tag, new_tag_list):
    return [(item[0], new_tag) if item[1] in new_tag_list else (item) for item in tp_list]


'''Q9'''


def get_tags_frequency(tp_list):
    my_dict = {}
    for item in tp_list:
        if item[1] not in my_dict:
            my_dict[item[1]] = 1
        elif item[1] in my_dict:
            my_dict[item[1]] += 1
    return my_dict


'''Q10'''


def display_histogram(int_list):
    for n in int_list:
        print("X" * n)


'''Q11'''


def display_histogram(my_data):
    for key in sorted(my_data.keys()):
        print(key + " " * (4 - len(key)) + "|" + "X" * my_data[key])


'''Q12'''


def create_my_tags_dictionary(my_list):
    returned = {}
    for item in my_list:
        if item[1] not in returned:
            returned[item[1]] = []
            returned[item[1]].append(item[0])
            returned[item[1]] = sorted(returned[item[1]])

        elif item[1] in returned:
            if item[0] not in returned[item[1]]:
                returned[item[1]].append(item[0])
                returned[item[1]] = sorted(returned[item[1]])
    return returned


'''Q13'''


def make_phrases(the_tags):
    tag_keys = sorted(the_tags.keys())
    for word1 in the_tags[tag_keys[0]]:
        for word2 in the_tags[tag_keys[1]]:
            for word3 in the_tags[tag_keys[2]]:
                print(word1, word2, word3)
