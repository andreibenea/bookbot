def get_book_words(text):
    counter = 0
    result = str(text).split()
    for word in result:
        counter += 1
    # print(f"{counter} words found in the document")
    return result, counter


def get_char_count(text):
    char_dict = {}
    lowercase_text = str(text).lower()
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_dict(unsorted_dict):
    dict_list = []
    for key, value in unsorted_dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    # print(dict_list)
    return dict_list
