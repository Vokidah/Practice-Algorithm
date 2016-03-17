__author__ = 'vokidah'


'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words
'''

def palindrome_permutation(string):
    dict = {}
    string = string.lower()
    for each in string:
        if each != " ":
            if each in dict:
                dict[each.lower()] += 1
            else:
                dict[each.lower()] = 1
    print(dict)
    flag = None
    string = string.replace(" ", "")
    even_or_odd = (len(string))%2
    for each in dict:
        if even_or_odd == 0:
            if dict[each]%2==1:
                return False
        else:
            if dict[each]%2 == 1:
                if flag:
                    return False
                else:
                    flag = True
    return True


print(palindrome_permutation("Tact Coa"))