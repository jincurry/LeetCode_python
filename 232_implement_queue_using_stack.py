# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top,
#  peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a
# stack by using a list or deque (double-ended queue), as long as you use only standard
# operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations
# will be called on an empty queue).

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.aStack, self.bStack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.aStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.bStack.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.bStack:
            while self.aStack:
                self.bStack.append(self.aStack.pop())
        return self.bStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.aStack and not self.bStack

