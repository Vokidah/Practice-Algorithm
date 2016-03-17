__author__ = 'vokidah'


'''
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def is_unique(string):
    array = list(string)
    array.sort()
    string = ''.join([x for x in array])
    for i in range(0,len(string)-1):
        if string[i]==string[i+1]:
            return False
    return True


print(is_unique("czadsv"))