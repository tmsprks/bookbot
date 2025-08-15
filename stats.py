def get_num_words(text):

    words = text.split()
    num_words = len(words)
    return num_words


def get_num_chars(text):
    characters = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for char in word:
            if char in characters:
                characters[char] = characters[char]+1
            elif char not in characters:
                characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    unsorted_array = []
    for char in dict:
        unsorted_array.append({"char": char, "num":dict[char]})
    unsorted_array.sort(reverse=True, key=sort_on)
    return unsorted_array

