class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        prefix = [0 for c in needle]

        left, right = 0, 1



        while right < len(needle):
            
            if needle[left] == needle[right]:
                prefix[right] = left + 1
                left += 1

            else:
                if left > 0 :
                    left = prefix[left-1]
                    continue
            right += 1

        
        n,h = 0,0

        while h < len(haystack):
            if needle[n] == haystack[h]:
                n += 1
                h += 1
            else:
                if n>0:
                    n = prefix[n-1]
                else:
                    h += 1
            
            
            if n == len(needle):
                return h - len(needle)
            
        return -1