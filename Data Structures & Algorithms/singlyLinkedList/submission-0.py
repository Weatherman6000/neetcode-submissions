class Node:

    def __init__(self, val: int):
        self.val = val

    def getVal(self):
        return self.val

class LinkedList:
    
    def __init__(self):
        self.list = []
        self.size = 0
    
    def get(self, index: int) -> int:
        if (index >= self.size): return -1
        return self.list[index].getVal()

    def insertHead(self, val: int) -> None:
        m = Node(val)
        self.list.insert(0, m)
        self.size += 1
    def insertTail(self, val: int) -> None:
        n = Node(val)
        self.list.append(n)
        self.size += 1

    def remove(self, index: int) -> bool:
        if (index >= self.size):
            return False
        self.list.pop(index)
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        valArr = [n.getVal() for n in self.list]
        return valArr
