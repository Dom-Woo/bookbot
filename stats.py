def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def sort_on(dict):
    return dict["count"]