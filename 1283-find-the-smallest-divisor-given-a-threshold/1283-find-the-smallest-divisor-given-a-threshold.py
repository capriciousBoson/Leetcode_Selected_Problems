class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        # if len(nums)==threshold: return right
        if sum(nums) < threshold: return 1

        res = right

        while left <=right :
            mid = (left + right)//2
            s = 0
            for n in nums :
                s += math.ceil(n/mid)
            print(f"mid :{mid}, s: {s}, threshold : {threshold}")
            if s <= threshold:
                res = min(res, mid)
                print(f" therefore updated res :{res}")
                right = mid-1

            else:
                left = mid+1
        return res

