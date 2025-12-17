class Solution:

    def countPartitions(self, arr, limit):
        partitions = 1
        count = 0
        for n in arr:
            if count+n <= limit:
                count += n
            else:
                partitions += 1
                count = n
        return partitions

    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        res = float('inf')

        while left <= right:

            mid = (left + right)//2
            partitions = self.countPartitions(nums, mid)
            print(f"left : {left}, right : {right}, mid: {mid} | partitions : {partitions}")
            if partitions == k:
                right = mid-1
                res = min(res, mid)
            elif partitions <k:
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
        
        print(f"max subarray sum limit : {res} ")

        ans = -float('inf')
        s = 0
        for n in nums:
            if s+n <= res:
                s += n
            else:
                s = n
            ans = max(ans, s)
        print(f"max subassray sum : {ans}")
        return ans

        