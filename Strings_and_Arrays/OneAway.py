__author__ = 'vokidah'

'''
There are three types of edits that can be peerformed on strings: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
'''


def one_away(string1, string2):
    if len(string1)>len(string2):
        for i in range(-1,len(string1)):
            if (string1[0:i+1]+string1[i+2:]) == string2:
                return True
    elif len(string1)<len(string2):
        for i in range(-1,len(string2)):
            if (string2[0:i+1]+string2[i+2:]) == string1:
                return True
    else:
        for i in range(0, len(string1)):
            if (string2[0:i]+string1[i]+string2[i+1:]) == string2:
                return True
    return False


print(one_away("pale", "bake"))