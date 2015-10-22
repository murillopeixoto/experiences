"""
The function scramble receives 2 strings values. It returns True if a portion of str1 characters
can be rearranged to match str2.
"""


def scramble(s1, s2):
    chars1 = chars_map(s1)
    chars2 = chars_map(s2)

    for char, count in chars2.items():
        if char not in chars1 or count > chars1[char]:
            return False

    return True


def chars_map(str):
    chars_map = {}

    for char in str:
        if char not in chars_map.has_key:
            chars_map[char] = 0
        chars_map[char] += 1

    return chars_map
