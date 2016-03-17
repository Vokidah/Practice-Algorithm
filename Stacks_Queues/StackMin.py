__author__ = 'vokidah'


'''
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in O(1) time.
'''


class SingleNode:

    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.minimum_for_him = data


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty:
            print("Empty Stack")
            return None
        data = self.top.data
        self.top = self.top.next
        return data


    def peek(self):
        if self.is_empty:
            print("Empty Stack")
            return None
        return self.top

    def push(self, data):
        if self.is_empty:
            self.top = SingleNode(data)
            return self.peek()
        else:
            new_node = SingleNode(data)
            new_node.next = self.top
            self.top = new_node
            if self.top.data > self.top.next.minimum_for_him:
                self.top.minimum_for_him = self.top.next.minimum_for_him
        return self.top.data

    def show(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next

    def minimum(self):
        return self.top.minimum_for_him