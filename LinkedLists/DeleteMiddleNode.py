__author__ = 'vokidah'


'''
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, end):
        n = self
        while n.next:
            n = n.next
        n.next = end

    def show(self):
        n = self
        while n:
            print(n.data)
            n = n.next


def delete_element_in_the_middle(node, n):
    if n and n.next:
        n.data = n.next.data
    if n.next.next:
        n.next = n.next.next