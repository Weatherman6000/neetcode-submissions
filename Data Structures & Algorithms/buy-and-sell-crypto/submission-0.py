class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profs = []
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profs.append(prices[j] - prices[i])
        profs.append(0)
        return max(profs)