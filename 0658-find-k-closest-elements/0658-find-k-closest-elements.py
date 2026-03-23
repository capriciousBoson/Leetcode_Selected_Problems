class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def iscloser(a,b,x):
            return abs(a-x) < abs(b-x) or (abs(a-x)==abs(b-x) and a<b)
        
        l = 0
        r = k

        while r< len(arr):
            # print(f"window : {arr[l:r]} checking for r = {arr[r]}")
            
            # if arr[r]==arr[r-1] and not iscloser(arr[r],arr[l], x):
            #     r += 1
            #     l +=1
            #     continue
            
            if not iscloser(arr[l], arr[r], x):
                r += 1
                l += 1
            else:
                break
        return arr[l:r]