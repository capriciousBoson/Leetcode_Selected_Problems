class Solution:
    def __init__(self):
        self.res = 0
    
    def merge(self, lh, rh):
        i,j = 0,0
        temp = []

        while i < len(lh) or j < len(rh) :
            if i==len(lh):
                temp.append(rh[j])
                j += 1
                continue
            elif j == len(rh):
                temp.append(lh[i])
                i += 1
                continue

            if lh[i] >= rh[j]:
                temp.append(rh[j])
                j += 1
            else:
                temp.append(lh[i])
                i += 1
    
        return temp

    def mergeSort(self, arr):
        # total_count = 0
        l,r = 0, len(arr)-1
        
        if l==r:
            return arr
        
        m = (l+r)//2
        lh = self.mergeSort(arr[l:m+1])
        rh = self.mergeSort(arr[m+1:r+1])
        self.res += self.countPairs(lh,rh)

        return self.merge(lh,rh)
    
    def countPairs(self, left, right):
        count = 0

        for i, n in enumerate(right):
            pos = bisect.bisect_left(left, 2*n+1)
            if pos < len(left):
                count += len(left)-pos
        return count


    def reversePairs(self, nums: List[int]) -> int:

        sorted_arr = self.mergeSort(nums)
        print(f"soryed  : {sorted_arr}")

        return self.res
            

                
