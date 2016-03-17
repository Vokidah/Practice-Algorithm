__author__ = 'vokidah'

'''
Implement a method to perform basic string compression using counts of repeated characters.
'''


def string_compression(string):
    count = 1
    string2 = ""
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            string2 +=(string[i]+str(count))
            count = 1
    string2 += (string[len(string)-1]+str(count))
    if len(string2) > len(string):
        return string
    return string2


print(string_compression("aabcccccaaa"))