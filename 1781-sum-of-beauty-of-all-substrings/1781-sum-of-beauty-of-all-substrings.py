class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)

        res = 0
        for i in range(n):

            counts = defaultdict(int)
            counts[s[i]] += 1
            maxf = 1
            minf = 1

            for j in range(i+1, n):

                counts[s[j]] += 1

                # print(f"substring : {s[i:j+1]}")

                maxf = max(maxf, counts[s[j]])
                minf = min(counts.values())

                res += maxf - minf

        return res








        