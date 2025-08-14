class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for r in ratings]
        right = [1 for r in ratings]


        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = 1+ left[i-1]


        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                right[j] = 1 + right[j+1]
        ans = [max(c1, c2) for c1,c2 in zip(left, right)]
        # print(f"candies : {ans}")
        return sum(ans)


         
        


        