class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stk = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in ops:
                stk.append(t)
                continue
            op1 = int(stk.pop())
            op2 = int(stk.pop())
            val = 1

            if t == '+':
                val = op2 + op1
            elif t=='-':
                val = op2 - op1
            elif t=='*':
                val = op2 * op1
            elif t=='/':
                val = int(op2/op1)
            stk.append(val)
        
        return int(stk[0])