from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        freq = defaultdict(int)
        max_freq = 0
        res = 0
        n = len(s)

        while r<n:
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            length = r-l+1
            # for valid answer we need length - max_freq <= k:
            # so while this is not satisfied we remove characcters from leftside
            if length-max_freq > k:
                freq[s[l]] -= 1
                # max_freq = max(freq.values())
                length -= 1
                l += 1
            
            if r-l+1-max_freq <= k:
                res = max(res, r-l+1)
            r +=1
        return res
            


        