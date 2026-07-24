class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        res = []
        for num in nums:
            if not freqDict.get(num): freqDict[num] = 1
            else: freqDict[num] += 1
        freqList = list(reversed(sorted(freqDict.values())))
        i = 0
        while i < k:
            for key in freqDict:
                if freqDict[key] == freqList[i]: 
                    i+= 1
                    res.append(key)
                    del freqDict[key]
                    break
        return res