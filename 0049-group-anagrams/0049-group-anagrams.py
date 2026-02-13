from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sig = [0 for _ in range(26)]
            for c in word:
                sig[ord(c)-ord('a')] += 1
            groups[tuple(sig)].append(word)

        return list(groups.values())
        