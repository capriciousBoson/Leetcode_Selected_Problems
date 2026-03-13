class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        start_times = collections.defaultdict(list)
        min_start = float('inf')
        for idx, [s,e,t] in enumerate(rides):
            start_times[s].append(idx)
            min_start = min(min_start, s)

        res = 0
        memo = {}

        def dfs(i):
            if i > n:
                return 0 
            
            if i not in start_times:
                return dfs(i+1)

            if i not in memo : 
                max_profit = 0
                for idx in start_times[i]:
                    s,e,t = rides[idx]
                    profit = e-s+t 
                    while e < n+2 and e not in start_times:
                        e += 1
                    profit += dfs(e)
                    max_profit = max(max_profit, profit)

                max_profit = max(max_profit, dfs(i+1))
                memo[i] = max_profit
            return memo[i]

        return dfs(min_start)


