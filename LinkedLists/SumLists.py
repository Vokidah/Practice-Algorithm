__author__ = 'vokidah'


'''
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
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


def sum_lists(node1, node2):
    help = 1
    result = 0
    while node1:
        result += node1.data*help
        help *= 10
        node1 = node1.next
    help = 1
    while node2:
        result += node2.data*help
        help *= 10
        node2 = node2.next
    node_result = Node(result%10)
    result = int(result/10)
    while result != 0:
        node_result.append_to_tail(result%10)
        result = int(result/10)
    return node_result
