from collections import defaultdict, Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False
        # counts = defaultdict(int)
        # for i in range(len(s)):
        #     counts[s[i]] += 1
        #     counts[t[i]] -= 1
        # for c in counts:
        #     if counts[c] : return False
        # return True
        return Counter(s)==Counter(t)
        