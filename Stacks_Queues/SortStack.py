__author__ = 'vokidah'

'''
Write a program to sort aa stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). THe stack supports the following operations: push, pop, peek, and isEmpty.
'''


class SingleNode:

    def __init__(self, data = None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            print("Empty Stack")
            return None
        return self.top

    def push(self, data):
        if self.is_empty():
            self.top = SingleNode(data)
            return self.peek()
        else:
            new_node = SingleNode(data)
            new_node.next = self.top
            self.top = new_node
        return self.top.data

    def show(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next


def sort(stack):
    temp = Stack()
    while not stack.is_empty:
        data = stack.pop()
        while not temp.is_empty() and temp.peek().data > data:
            stack.push(temp.pop())
        temp.push(data)
    return temp