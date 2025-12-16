class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        k = r

        while l<=r:
            
            mid = (l+r)//2
            # check if mid is possible
            h_ = 0
            for bananas in piles:
                h_ += math.ceil(bananas / mid)
            if  h_ <= h:
                k = min(k, mid)
                r = mid-1
            else:
                l = mid+1
        return k