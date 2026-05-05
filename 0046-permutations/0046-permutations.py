class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        idxs = [i for i in range(n)]
        res = []

        def permutate(indexes, permutation):
            if len(permutation)==n:
                res.append(permutation[:])
                return
            
            for i in range(n):
                if indexes[i] != -1:
                    permutation.append(nums[indexes[i]])
                    indexes[i] = -1
                    permutate(indexes, permutation) 
                    permutation.pop()
                    indexes[i] = i
        permutate([i for i in range(n)], [])
        return res



        