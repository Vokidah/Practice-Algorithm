__author__ = 'vokidah'

'''
Write code to remove duplicates from an unsorted linked list.
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


def remove_duplicates(node):
    first = node
    while first:
        second = first
        while second.next:
            if second.next.data == first.data:
                second.next = second.next.next
            else:
                second = second.next
        first = first.next
    return














