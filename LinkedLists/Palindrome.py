__author__ = 'vokidah'

'''
Implement a function to check if a linked list is a palindrome.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def show(self):
        n = self
        while n:
            print(n.data)
            n = n.next

    def append_to_tail(self, end):
        n = self
        while n.next:
            n = n.next
        n.next = end


def palindrome(node):
    i = 0
    first = node
    second = node
    stack = []
    while first:
        if i%2 == 1:
            second = second.next
        first = first.next
        i += 1
    first = node
    if i%2 == 1:
        second = second.next
    for j in range(int(i/2)):
        stack.append(second)
        second = second.next
    for i in range(0, len(stack)):
        if stack.pop().data != first.data:
            return False
        first = first.next
    return True
