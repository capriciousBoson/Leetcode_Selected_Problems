class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        freqs = []

        res = 0
        for w in range(2, n):
            l = 0
            r = w
            current_counts = collections.Counter(s[l:r+1])
            while r < n:
                maxf = max(current_counts.values())
                minf = min(current_counts.values())

                # print(f" substring : {s[l:r+1]}")
                # print(f"current_counts : {current_counts}")

                # print(f"max, min  : {maxf, minf} | res :{res}")
                res += maxf-minf
                # print(f"max, min  : {maxf, minf} | res :{res}")

                
                current_counts[s[l]] -= 1
                if current_counts[s[l]] == 0:
                    current_counts.pop(s[l])
                l += 1
                r += 1
                if r <n:    
                    current_counts[s[r]] += 1
        return res




        