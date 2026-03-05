class Solution:
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        left_min = [-1 for n in arr]
        right_min = [-1 for n in arr]
        
        n = len(arr)
        stk = [n]

        for i in range(n-1, -1, -1):
            while stk[-1]!= n and arr[stk[-1]] > arr[i]:
                stk.pop()
            right_min[i] = stk[-1]
            stk.append(i)
        
        stk = [-1]
        for i in range(n):
            while stk[-1]!= -1 and arr[stk[-1]] >= arr[i]:
                stk.pop()
            left_min[i] = stk[-1]
            stk.append(i)
        
        res = 0
        for i in range(n):
            res += (i-left_min[i]) * ( right_min[i]-i)*arr[i]
        return res%MOD





        