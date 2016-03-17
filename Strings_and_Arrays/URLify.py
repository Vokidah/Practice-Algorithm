__author__ = 'vokidah'


'''
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
'''

def URLify(string, length):
    for i in range(0, length):
        if string[i] == " ":
            string = string[0:i]+"%20"+string[i+1:]
    return string


print(URLify("Mr John Smith    ", 13))