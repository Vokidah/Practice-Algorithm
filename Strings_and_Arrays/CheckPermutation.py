__author__ = 'vokidah'

'''
Given two strings,
write a method to decide if one is a permutation of the other
'''

def check_permutation(string1, string2):
    string1.sort()
    string2.sort()
    if string1 == string2:
        return True
    return False


print(check_permutation("adda","daada"))