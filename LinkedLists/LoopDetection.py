__author__ = 'vokidah'

'''
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
'''


class Loop_Node:
    def __init__(self, data):
        self.next = self
        self.data = data


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


def loop_detection(node):
    hash = {}
    while node:
        if node not in hash:
            hash[node] = True
        elif hash[node]:
            return node
        node = node.next
    return None