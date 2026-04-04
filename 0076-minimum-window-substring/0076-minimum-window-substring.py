class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""


        min_len = float('inf')
        min_str = ""

        t_counter = collections.Counter(t)
        left,right = 0,0
        formed = 0
        window_counter = collections.defaultdict(int)

        while right < len(s):
            # expand the window
            rchar = s[right]
            if rchar in t_counter:
                window_counter[rchar] += 1
                if window_counter[rchar]==t_counter[rchar]:
                    formed += 1

            # shrink the window
            while formed==len(t_counter) and left <= right:
                if right-left + 1 < min_len:
                    min_len = right-left + 1
                    min_str = s[left:right+1]
                
                lchar = s[left]
                left += 1

                # adjust counters upon shrinking
                if lchar in window_counter:
                    window_counter[lchar] -= 1
                    if window_counter[lchar] < t_counter[lchar]:
                        formed -= 1

            right += 1

        return min_str


                


        