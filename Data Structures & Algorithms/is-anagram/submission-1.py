class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqueS = set(s)
        uniqueT = set(t)
        if not uniqueS == uniqueT:
            return False
        for v in uniqueS:
            if not s.count(v) ==  t.count(v):
                return False
        return True