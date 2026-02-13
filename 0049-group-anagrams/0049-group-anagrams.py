from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            key = [0 for i in range(26)]
            for c in word:
                key[ord(c)-ord('a')]+=1
            anagram_groups[tuple(key)].append(word)
        return anagram_groups.values()

                



        