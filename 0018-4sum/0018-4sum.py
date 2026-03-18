class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []


        n = len(nums)
        for a in range(n-3):

            if sum(nums[a:a+4]) > target: break
            if nums[a]+sum(nums[n-3:]) < target: continue
            
            if a > 0 and nums[a] == nums[a-1]: 
                # print(f"skipping a : {a}")
                continue

            # print(f"\na  {nums[a]} -----------------")
            for b in range(a+1, n-2):
                

                if b>a+1 and nums[b]==nums[b-1]:
                    # print(f"skipping b :{b}") 
                    continue
                # print(f"b  {nums[b]} --")

                c, d = b+1 , n-1
                # print(f"c, d : {c,d}")

                while c < n and d>0  and c<d:


                    # print(f"a,b,c,d : {a,b,c,d}")
                    x = nums[a] + nums[b] + nums[c] + nums[d]
                    # print(f"sum of : {nums[a] , nums[b] , nums[c] , nums[d]} = {x}")

                    if x == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                    if x < target:
                        c += 1
                    if x > target:
                        d -= 1

                    
                    while b+1 < c < n and nums[c]==nums[c-1]:
                        c += 1
                
                    while 0 < d < n-1 and nums[d]==nums[d+1]:
                        d -= 1


        return res

         
        