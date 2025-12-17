class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left, right = 0,  len(arr)-1

        while left <= right:
            mid = (left+right)//2

            missing = arr[mid]-(mid +1)
            print(f"mid : {mid}, missing at mid : {missing}")

            if missing <k:
                left = mid+1
            else:
                right = mid-1
                
        print(f"left: {left}, right : {right}")
        m1 = arr[right]-(right+1)  #account for 0 based indeing
        print(f"m1 : {m1}")
        res = k-m1 + arr[right]
        return res

        