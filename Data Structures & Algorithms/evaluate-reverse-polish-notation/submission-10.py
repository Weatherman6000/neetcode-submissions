class Stack:
    
    def __init__(self):
        self.workList = []
        self.size = 0

    def push(self, val):
        self.workList.append(val)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.workList.pop()
    
    def curr(self):
        return self.workList
            
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        clac = Stack()
        tokens.reverse()
        print(tokens)
        while len(tokens) > 0:
            tok1 = tokens.pop()
            if tok1 not in ['+', '-', '*', '/']: clac.push(int(tok1))
            elif tok1 == '+': 
                second = clac.pop()
                first = clac.pop()
                clac.push(first + second)
            elif tok1 == '-': 
                second = clac.pop()
                first = clac.pop()
                clac.push(first - second)
            elif tok1 == '*': 
                second = clac.pop()
                first = clac.pop()
                clac.push(first * second)
            elif tok1 == '/': 
                second = clac.pop()
                first = clac.pop()
                clac.push(int(first / second))
            print("current wlist:", clac.curr())
        return clac.pop()

        


        