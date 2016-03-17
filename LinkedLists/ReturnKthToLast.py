__author__ = 'vokidah'

'''
Implement an algorithm to find the k-th to last element of a singly linked list
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


def return_k_th_to_last(node, k):
    current = node
    length = 0
    while current:
        current = current.next
        length += 1
    length = length - k
    if length <= 0:
        return None
    current = node
    while length > 0:
        current = current.next
        length -= 1
    print("%s-th to the last is %s"%(k, current.data))
    return current.data

