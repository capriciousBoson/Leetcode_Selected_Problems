class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1
        left, right = min(bloomDay), max(bloomDay)
        res = float('inf')

        while left <=right:

            mid = (left+right)//2 
            # print(f"\nleft : {left}, right: {right}, mid: {mid}")

            # check if mid is possible
            b = 0
            flowers = 0
            for d in range(n):
                # print(f"CURRENT : bouquets :{b}, flowers:{flowers}")
                
                if bloomDay[d] <= mid:
                    flowers += 1
                else:
                    flowers = 0

                if flowers == k:
                    b += 1
                    flowers = 0
            # print(F"made bouquets : {b}")    
            if b >= m:
                right = mid-1
                res = min(res, mid)
                # print(f"found a res : {res}")
            else:
                left = mid+1
        return -1 if res==float('inf') else res

        