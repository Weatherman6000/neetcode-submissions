class Stack:
    def __init__(self):
        self.worklist = []
        self.size = 0
    
    def push(self, v):
        self.worklist.append(v)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if not self.isEmpty():
            n = self.worklist[self.size-1]
            return n

    def pop(self):
        n = self.worklist.pop(self.size - 1)
        self.size -= 1
        return n



class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '{', '['}
        closing = {')', '}', ']'}
        close2open = { ')':'(',
                       '}':'{',
                       ']':'[' }
        stk = Stack()
        for c in s:
            if c in opening:
                stk.push(c)
            else:
                if stk.peek() == close2open[c]:
                    stk.pop()
                else: return False
        return stk.isEmpty()
            
