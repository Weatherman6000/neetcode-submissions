class Solution:

    def findAnagram(self, w1, w2):
        if not len(w1) == len(w2): return False
        for c in w1:
            if not w2.count(c) == w1.count(c): return False
        return True 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        while len(strs) > 0:
            group = []
            ana = strs.pop(0)
            group.append(ana)
            for i in range(len(strs)- 1, -1, -1):
                gram = strs[i]
                if self.findAnagram(ana, gram): 
                    strs.remove(gram)
                    group.append(gram)
            res.append(group)
        return res
    
