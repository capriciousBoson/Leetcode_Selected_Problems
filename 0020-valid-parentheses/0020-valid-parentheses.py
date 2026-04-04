class Solution:
    def isValid(self, s: str) -> bool:

        open_ = {'(':')', '{':'}', '[':']'}

        if s[0] not in open_ : 
            return False
        

        stk = [s[0]]

        for i  in range(1, len(s)):
            if s[i] in open_ : 
                stk.append(s[i])
            else:
                if not stk:
                    return False
                if  open_[stk[-1]] !=s[i] :
                    return False
                else:
                    stk.pop()
        
        return len(stk)==0