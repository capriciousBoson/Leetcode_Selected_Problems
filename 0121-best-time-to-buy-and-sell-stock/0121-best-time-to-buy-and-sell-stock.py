class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0

        for i in range(1, len(prices)):
            # print(f"min_price : {min_price} | prices[i] : {prices[i]}")
            res = max(res, (prices[i] - min_price))
            min_price = min(min_price, prices[i])
        
        return res if res > 0 else 0



        