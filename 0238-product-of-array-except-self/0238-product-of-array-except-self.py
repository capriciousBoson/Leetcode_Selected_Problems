class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1 for _ in range(n)]
        postfix = [1 for _ in range(n)]

        # if n>1:
        #     prefix[1] = nums[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        # if n>1:
        #     postfix[n-2] = nums[n-1]
        
        for j in range(n-2, -1, -1):
            postfix[j] = postfix[j+1] * nums[j+1]

        # print(f"prefix : {prefix} \npostfix :{postfix}")
        
        res = []
        for i in range(n):
            res.append(prefix[i]*postfix[i])
        return res

