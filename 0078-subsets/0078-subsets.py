class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(list)
        res = []

        def dfs(i,subset):
            if i==n:
                res.append(subset)
                return
            
            dfs(i + 1, subset + [nums[i]])
            dfs(i+1, subset)
            return 
        
        dfs(0,[])
        return res
        