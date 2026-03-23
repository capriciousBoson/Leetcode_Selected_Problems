class Solution:
    def validPalindrome(self, s: str) -> bool:

        removed = 0
        memo = {}

        def dfs(l,r):

            nonlocal removed
            if l > r:
                return True

            if (l,r) not in memo:
                    
                if s[l]==s[r]:
                    memo[(l,r)] =  dfs(l+1, r-1)
                
                else:
                    if removed >= 1:
                        return False
                    else:
                        removed += 1
                        ans = False
                        if s[l+1] == s[r]:
                            ans = ans or dfs(l+1, r)
                        if s[l] == s[r-1]:
                            ans = ans or dfs(l, r-1)
                        memo[(l,r)] = ans 
            return memo[(l,r)]
                    
        return dfs(0, len(s)-1)

        