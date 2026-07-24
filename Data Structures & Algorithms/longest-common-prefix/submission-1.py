class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        iters = len(strs[0])
        while iters > 0: 
            prefix = strs[0][0]
            for i in range(len(strs)):
                if not strs[i].startswith(prefix):
                    return common
                strs[i] = strs[i][1:]
            common += prefix
            iters -= 1
        return common