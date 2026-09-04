class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1 for _ in range(n)]
        right_product = [1 for _ in range(n)]
        res = [1 for _ in range(n)]

    
        for i in range(1, len(nums)):
            p = left_product[i-1] * nums[i-1]
            left_product[i]=p
        
        
        

        for j in range(len(nums)-2, -1, -1):
            p = right_product[j+1] * nums[j+1]
            right_product[j]=p
        
        res = []
        for l,r in zip(left_product, right_product):
            res.append(l*r)
        
        return res