class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        

        max_product = nums[0]

        back_prod = [1 for n in nums]
        front_prod = [1 for n in nums]

        

        total_product = nums[0]

        for i in range(1, len(nums)):
            pf = back_prod[i-1]*nums[i-1] 
            if pf ==0:
                pf = nums[i-1]
            back_prod[i] = pf
            # back_prod[i] = max(back_prod[i-1]*nums[i-1], nums[i-1])
            total_product *= nums[i]

        for j in range(len(nums)-2, -1, -1):
            sf = front_prod[j+1]*nums[j+1]
            if sf == 0:
                sf = nums[j+1]
            front_prod[j] = sf
            # front_prod[j] = max(front_prod[j+1]*nums[j+1], nums[j+1])

        back_prod[0] = -float('inf')
        front_prod[-1] = -float('inf')

        # print(f"prefix prod : {back_prod}")
        # print(f"suffix prod : {front_prod}")
        for i,n in enumerate(nums):

            max_product = max(max_product, back_prod[i],front_prod[i] , n)

        max_product = max(max_product, total_product)

        return max_product
        


        
        