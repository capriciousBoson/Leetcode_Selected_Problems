from functools import lru_cache
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # pi = {i:0 for i in range(n)}

        prefix = [[sum(pile[0:i+1]) for i in range(len(pile))] for pile in piles]
        print(prefix)
        memo = {}
        # @lru_cache(None)
        def dfs(count, pile_idx):
            if count <0  or pile_idx>=n:
                return 0

            # print(f"\nnums to take : {count} | currently at piles[{pile_idx}] : {piles[pile_idx]}")
            
            if (count, pile_idx) not in memo:
                s = dfs(count, pile_idx+ 1)
                limit = min(count, len(piles[pile_idx]))
                for i in range(1,limit+1):
                    # if i <= len(prefix[pile_idx]):
                        
                        # print(f"taking {i} for current pile with sum : {sum(piles[pile_idx][0:i])}")
                    s = max(s, prefix[pile_idx][i-1] + dfs(count-i, pile_idx+1) )
                        # print(f"finally got s = {s} for pile : {piles[pile_idx]} for first : {i} of :{count-i}")
                memo[(count, pile_idx)] = s
            return memo[(count, pile_idx)]
            # return s
        
        return dfs(k, 0)




        # def dfs(i):
        #     if i>=k :
        #         return 0

        #     s = 0
        #     for j in range(n):
        #         if len(piles[j]) > pi[j] :

        #             x = piles[j][pi[j]]

        #             pi[j] += 1
        #             s = max(s, x + dfs(i+1))
        #             pi[j] -= 1

        #     return s

        # return dfs(0)

        