class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = []
        for i in range(n-1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            
            if stk:
                res.append(stk[-1]-i)
            else:
                res.append(0)

            stk.append(i)
        return res[::-1]