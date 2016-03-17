__author__ = 'vokidah'

'''
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimicks this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
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


class SetOfStacks:

    def __init__(self, capacity):
        self.set_of_stacks = [Stack()]
        self.sizes = [0]
        self.max_capacity = capacity

    def push(self, data):
        if self.sizes[-1] != self.max_capacity:
            self.set_of_stacks[-1].push(data)
            self.sizes[-1] += 1
        else:
            self.set_of_stacks.append(Stack())
            self.set_of_stacks[-1].push(data)
            self.sizes[-1] = 1
        return self.set_of_stacks[-1].peek().data

    def show(self):
        for i in range(0, len(self.set_of_stacks)):
            print("STACK №%s" % (i+1))
            print(self.set_of_stacks[i].show)
            print('')
        return

    def pop(self):
        stack = self.set_of_stacks[-1]
        data = stack.pop()
        if self.sizes[-1] - 1 == 0:
            self.sizes.remove(self.sizes[-1])
            self.set_of_stacks.remove(stack)
        return data


set_of_stacks = SetOfStacks(5)
set_of_stacks.push(2)
set_of_stacks.push(1)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(3)
set_of_stacks.push(6)
set_of_stacks.push(1)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(3)
set_of_stacks.push(6)
set_of_stacks.push(1)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(3)
set_of_stacks.push(6)

set_of_stacks.show()