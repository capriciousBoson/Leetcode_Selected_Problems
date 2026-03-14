class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for c in s:
            # print(f"c : {c} | stk : {stk}")

            if c == '(':
                stk.append(c)
            if c == ')':
                if stk and stk[-1]=='(':
                    stk.pop()
                else:
                    stk.append(c)
        return len(stk)
            

