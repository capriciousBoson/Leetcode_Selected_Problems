class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = float('inf')
        
        def bsearch(l, r):
            nonlocal k
            if l>r:
                return 
            
            mid = (l+r)//2
            # check if mid is possible
            h_ = 0
            for p in piles:
                h_ += p//mid if p%mid==0 else (p//mid)+1
            
            if h_ <= h:
                k = min(k, mid)
                return bsearch(l, mid-1)
            elif h_ > h:
                return bsearch(mid+1, r)
        bsearch(1, max(piles))   
        return k


        