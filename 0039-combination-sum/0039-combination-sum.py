class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        res = []

        def dfs(i, x, subset):
            if x==target:
                res.append(subset)
                return
            
            if x > target:
                return

            if i==n:
                return
            
            dfs(i, x + candidates[i], subset+[candidates[i]])
            dfs(i+1, x, subset)
        dfs(0, 0, [])
        return res
     