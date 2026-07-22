class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(2**n):
            bits = f'{i:0{n}b}'
            subset = [nums[j] for j in range(n) if bits[j] == '1']
            res.append(subset)
        return res

        # def dfs(i,subset):
        #     if i==n:
        #         res.append(subset)
        #         return
            
        #     dfs(i + 1, subset + [nums[i]])
        #     dfs(i+1, subset)
        #     return 
        
        # dfs(0,[])
        # return res
        