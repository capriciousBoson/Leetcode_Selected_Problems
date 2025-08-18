class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = "".join([ch for ch in s if ch.isalnum()])
        # print(f"s : {s}")
        l, r = 0, len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return False
            l += 1
            r -= 1
        return True
        