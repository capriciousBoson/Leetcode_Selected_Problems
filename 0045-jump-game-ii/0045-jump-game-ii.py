class Solution:
    # def find_jump(self,ranges, i):
    #     for a,b,jumps in ranges:
    #         if a<=i<=b : return jumps

    def jump(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n==1:
        #     return 0

        # max_reach = 0 
        # ranges = [[0,0,0]]

        # for i in range(n):
        #     if i + nums[i] > max_reach:
        #         current_jumps = 0
        #         for a,b,j in ranges:
        #             if a<=i<=b:
        #                 current_jumps = j
        #                 break
        #         current_jumps += 1
        #         max_reach = i+nums[i]
        #         ranges.append([i, max_reach, current_jumps])

        #         if max_reach >= n-1:
        #             return current_jumps
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        end = 0        # end of the current jump's range
        farthest = 0   # farthest we can reach while scanning this range

        # We stop at n-2 because once we reach the last index, no more jumps are needed
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
                if end >= n - 1:
                    break
        return jumps




