class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def fun(i,t, subset):
            if i >= len(candidates):
                return
            if t==target:
                res.append(subset)
                return
            elif t > target:
                return
            fun(i+1, t, subset) 
            fun(i, t+candidates[i], subset+[candidates[i]]) 
            
        fun(0, 0, [])
        return res