class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        res = right

        while left<=right:
            mid = (left+right)//2
 
            w, d = 0,0

            for p in weights:
                w += p
                if w == mid:
                    w = 0
                    d += 1
                elif w>mid :
                    w = p
                    d += 1
            if w: 
                w = 0
                d += 1

            # print(f"capacity : {mid}, days  taken : {d}, total days: {days}" )
            if d <= days:
                res = min(res, mid)
                right = mid-1
            else:
                left = mid + 1
        return res




        