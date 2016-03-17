__author__ = 'vokidah'

'''
Implement a MyQueue class which implements a queue using two stacks.
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


class MyQueue:

    def __init__(self, data):
        self.first = Stack()
        self.first.push(data)
        self.second = Stack()

    def add(self, data):
        current = self.first.peek()
        while current:
            self.second.push(self.first.pop())
            current = current.next
        self.second.push(data)
        current = self.second.peek()
        while current:
            data = self.second.pop()
            self.first.push(data)
            current = current.next
        return data

    def remove(self):
        data = self.first.pop()
        return data

    def show(self):
        current = self.first.peek()
        while current:
            print(current.data)
            current = current.next