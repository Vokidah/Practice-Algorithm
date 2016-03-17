__author__ = 'vokidah'


'''
Write code to partition a linked list around a value x, such that all nodes less than x come before
all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the "right
partition"; it does not need to apper between the left and right partitions.
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


def partition(node, x):
    first = node
    if not first.next:
        return
    while first:
        if first.data >= x:
            second = first.next
            while second:
                if second.data < x:
                    data = second
                    break
                second = second.next
            temp = data.data
            data.data = first.data
            first.data = temp
        first = first.next
    return