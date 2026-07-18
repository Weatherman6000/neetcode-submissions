class MinStack:

    def __init__(self):
        self.workList = []
        self.size = 0

    def push(self, val: int) -> None:
        self.workList.append(val)
        self.size += 1

    def pop(self) -> None:
        self.workList.pop()
        self.size -= 1

    def top(self) -> int:
        n = self.workList[self.size -1]
        return n

    def getMin(self) -> int:
        return min(self.workList)
