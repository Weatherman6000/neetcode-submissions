class Stack:
    
    def __init__(self, workList = None):
        self.workList = workList if not workList == None else []
        self.size = len(self.workList)

    def __repr__(self):
        return f"Current stack is: {self.workList}" 

    def push(self, val):
        self.workList.append(val)
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.workList.pop()

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numDays = len(temperatures)
        temperatures.reverse()
        tempStk = Stack(temperatures)
        print("Curr TempList: ", tempStk)
        discardStk = Stack()
        res = [0] * numDays
        for i in range(numDays):
            counter = 0
            currTemp = tempStk.pop()
            Found = False
            while not tempStk.isEmpty() and Found == False:
                nextTemp = tempStk.pop()
                counter += 1
                discardStk.push(nextTemp)
                if nextTemp > currTemp:
                    res[i] = counter
                    Found = True 
            while not discardStk.isEmpty():
                tempStk.push(discardStk.pop())
            print("Curr TempList:", tempStk)
        return res
