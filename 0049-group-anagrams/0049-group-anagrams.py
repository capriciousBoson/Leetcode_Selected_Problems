class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = collections.defaultdict(list)

        for  s in strs:
            # key = [0 for _ in range(26)]
            # for char in s:
            #     key[ord(char)-97] += 1
            
            # key = 
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())