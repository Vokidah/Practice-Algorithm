__author__ = 'vokidah'


'''
Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the k-th of the first linked list is the exact same node (by reference) as the
j-th node of the second linked list, then they are intersecting.
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


def intersection(node1, node2):
    length1, length2 = 1, 1
    node_1 = node1
    while node_1.next:
        length1 += 1
        node_1 = node_1.next
    node_2 = node2
    while node_2.next:
        length2 += 1
        node_2 = node_2.next
    if node_1 != node_2:
        return None
    length = abs(length1-length2)
    for i in range(0, length):
        if length1 > length2:
            node1 = node1.next
        elif length2 > length1:
            node2 = node2.next
    while node1:
        if node1 == node2:
            return node1.data
        node1 = node1.next
        node2 = node2.next
    return None
