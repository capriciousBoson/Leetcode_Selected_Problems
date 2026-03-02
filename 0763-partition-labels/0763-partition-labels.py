class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = collections.Counter(s)
        current_counts = collections.defaultdict(int)
        res = []
        prev = -1
        for i in range(len(s)):
            current_counts[s[i]] += 1
            if current_counts[s[i]] == counts[s[i]]:
                del current_counts[s[i]]
            
            if len(current_counts) == 0:
                res.append(i-prev)
                prev = i
        return res
        