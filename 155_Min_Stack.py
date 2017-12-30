# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# __title__ = ''
# __author__ = 'king'
# __mime__ = '17-12-30'
# """

#  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     getMin() -- Retrieve the minimum element in the stack.
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        """
        :rtype: int
        """
        x = self.stack[-1]
        if x > 0:
            return self.min + x
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    obj = MinStack()
    obj.push(4)
    obj.push(6)
    obj.push(1)
    print(obj.getMin())
    print(obj.top())
    obj.pop()
    print(obj.getMin())
    print(obj.top())
