class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_str = ""
        n = len(s)

        
        for i in range(n):
            start_points = [[i,i], [i,i+1]]

            for l,r in start_points :
                while l>=0 and r<n and s[l]==s[r]:
                    # print(f"str : {s[l:r+1]}")

                    length = r-l + 1
                    if  length > max_length:
                        max_length = length
                        max_str  = s[l:r+1]
                    l -=1
                    r +=1
                    

        return max_str