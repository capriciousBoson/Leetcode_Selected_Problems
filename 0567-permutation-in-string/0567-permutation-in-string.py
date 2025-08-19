from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = set(s1)
        counts1 = Counter(s1)
        n = len(s2)
        left, right = 0,0

        counts2 = defaultdict(int)
        # print(f"s1 counter : {counts1}")

        while right < n:
            # print(f"\ncurrent substring : {s2[left:right+1]}")
            # print(f"left :{left} right :{right}")
            # print(f"counts2 : {counts2}")
            # print(f"processing: {s2[right]}")
            char = s2[right]
            if char  in s1_chars:
                counts2[char] += 1

                while left < right and counts2[char] > counts1[char]:
                    counts2[s2[left]] -= 1
                    left += 1
                # print(f"updated counter : {counts2} left, right = {left, right}")
                if counts2 == counts1:
                    return True
            else:
                left = right+1
                counts2 = defaultdict(int)
            right = right+1
        return False
        
                    

                    





        