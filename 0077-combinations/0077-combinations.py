class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combinations(comb, i):
            nonlocal res
            if len(comb)==k:
                res.append(comb)
                return
            
            if i >n:
                return

            combinations(comb+[i], i+1)
            combinations(comb, i+1)
            return
        combinations([], 1)
        return res