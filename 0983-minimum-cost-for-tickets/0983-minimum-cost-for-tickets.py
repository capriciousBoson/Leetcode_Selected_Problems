class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        memo = {}
        numdays = [1,7,30]

        def dfs(i):
            if i >= n:
                return 0

            # if i ==0:
            #     print(f"\ni : {i} days : {days[i]}")
            
            
            if i not in memo:
                # buying 1 day pass
                
                x = costs[0] + dfs(i+1)
                # if i==0: print(f"cost of taking 1 day pass : {x}")
                # x = float('inf')

                #buying 7, 30 day pass
                for d in range(1,3) :
                    max_days = days[i] + numdays[d]-1
                    i_ = i
                    for j in range(i, n):
                        if days[j] <= max_days:
                            i_ = j
                        else:
                            break
                    x = min(x, costs[d] + dfs(i_ +1))
                    # if i==0: print(f"cost of taking {numdays[d]} day pass : {x}")
                memo[i] = x
            # print(f"memo[{i}] : {memo[i]}")
            return memo[i]

        return dfs(0)