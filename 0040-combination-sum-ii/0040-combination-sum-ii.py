class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

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
            
            for idx in range(i, n):

                if idx > i and candidates[idx]==candidates[idx-1]:
                    continue
                dfs(idx+1, x+candidates[idx], subset + [candidates[idx]])


        dfs(0, 0, [])
        return res
        