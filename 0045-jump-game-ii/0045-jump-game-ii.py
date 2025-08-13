class Solution:
    def find_jump(self,ranges, i):
        for a,b,jumps in ranges:
            if a<=i<=b : return jumps

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0

        max_reach = 0 
        ranges = [[0,0,0]]

        for i in range(n):
            if i + nums[i] > max_reach:
                current_jumps = self.find_jump(ranges, i)
                current_jumps += 1
                max_reach = i+nums[i]
                ranges.append([i, max_reach, current_jumps])

                if max_reach >= n-1:
                    return current_jumps




