from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        t_counter = Counter(t)
        window_counter = defaultdict(int)

        required = len(t_counter)
        found = 0

        left, right = 0,0
        min_len = float('inf')
        min_window = ""

        while right < n :
            # print(f"\ncurrent window : {s[left:right+1]}")
            char = s[right]
            if char in t_counter:
                window_counter[char] += 1
            
                if window_counter[char] == t_counter[char]:
                    found += 1
            while found == required and left <= right:
                # print(f"found candidate : {s[left:right+1]} window_counter : {window_counter}")
                if right-left+1 < min_len:
                    min_len  = right-left+1
                    min_window = s[left:right+1]

                # shrink thw window by 1
                left_char = s[left]
                if left_char in window_counter:
                    window_counter[left_char] -= 1
                    if window_counter[left_char] < t_counter[left_char]:
                        found -= 1
                left += 1
            right += 1
        return min_window



                  


                
        