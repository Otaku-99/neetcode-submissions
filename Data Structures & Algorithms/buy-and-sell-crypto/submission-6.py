class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out=0
        j=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>j:
                out=max(out,prices[i]-j)
            else:
                j=min(j,prices[i])
        return out