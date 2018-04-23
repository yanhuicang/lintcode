#!/usr/bin/env python
# -*-coding:utf-8 -*-
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = list()
        self.head = -1

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.head += 1
        if self.head == 0:
            tmp = (number, number)
        else:
            if number < self.stack[self.head - 1][1]:
                tmp = (number, number)
            else:
                tmp = (number, self.stack[self.head - 1][1])
        if self.head >= len(self.stack):
            self.stack.append(tmp)
        else:
            self.stack[self.head] = tmp
        
        
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.head < 0:
            return
        self.head -= 1
        return self.stack[self.head + 1][0]

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if self.head < 0:
            return
        return self.stack[self.head][1]
        
        
if "__main__" == __name__:
    s = MinStack()
    s.push(-1)
    s.push(-2)
    print s.min()
    print s.pop()
    s.push(-3)
    s.push(3)
    s.push(2)
    print s.pop()
    print s.pop()
    print s.pop() 
