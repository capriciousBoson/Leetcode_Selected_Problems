class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def combinations(i, t, subset):
            if t==target:
                res.append(subset[:])
                return
            if i >= n:
                return
            if t > target:
                return
            

            
            for idx in range(i, n):
                if idx > i and candidates[idx]==candidates[idx-1]:
                    continue
                # if t+candidates[idx] > target:
                #     break
                combinations(idx+1, t+candidates[idx], subset + [candidates[idx]])
            return 
        combinations(0, 0, [])
        return res