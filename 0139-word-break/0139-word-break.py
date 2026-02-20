class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        memo = {}
        def dfs(i,j):
            if i >= n:
                return True
            if j >= n:
                return False

            if (i,j) not in memo:
                if s[i:j+1] in words:
                    memo[(i,j)] = dfs(i, j+1) or dfs(j+1, j+1)
                else:
                    memo[(i,j)] =  dfs(i, j+1)
            return memo[(i,j)]
        return dfs(0,0)

