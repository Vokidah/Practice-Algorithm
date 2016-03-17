__author__ = 'vokidah'


'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
'''


def string_rotation(string1, string2):
    return is_substring(string1+string1, string2)


def is_substring(string2, string1):
    if string1 in string2:
        return True
    return False


print(string_rotation("waterbottle", "erbottlewat"))