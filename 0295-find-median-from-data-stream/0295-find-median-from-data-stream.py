class MedianFinder:

    def __init__(self):
        self.left_half = []
        self.right_half = []
        self.left_size = 0
        self.right_size = 0 
        

    def addNum(self, num: int) -> None:
        # print(f"\ntrying to all dun : {num}----------------------------")
        if self.left_size ==0 and self.right_size==0:
            heapq.heappush(self.right_half, num)
            self.right_size += 1

        elif num >= self.right_half[0]:
            heapq.heappush(self.right_half, num)
            self.right_size += 1

        else :
            heapq.heappush(self.left_half, -num)
            self.left_size += 1
        
        # print(f"After adding {num}   ------")
        # print(f"left : {self.left_half} size: {self.left_size}")
        # print(f"right : {self.right_half} size : {self.right_size}")

        while abs(self.left_size - self.right_size) > 1:
            if self.left_size > self.right_size:
                n = -1*heapq.heappop(self.left_half)
                self.left_size -= 1
                # print(f"transfering {n} from left to right")
                heapq.heappush(self.right_half, n)
                self.right_size += 1
            else:
                n = -1*heapq.heappop(self.right_half)
                self.right_size -= 1
                # print(f"transfering {n} from right to left")
                heapq.heappush(self.left_half, n)
                self.left_size += 1

        # print(f"After balancing -----------")
        # print(f"left : {self.left_half} size: {self.left_size}")
        # print(f"right : {self.right_half} size : {self.right_size}")



        

    def findMedian(self) -> float:
        # print(f"\nfinding median ------------------------------")
        # print(f"left : {self.left_half} size: {self.left_size}")
        # print(f"right : {self.right_half} size : {self.right_size}")
        
        median = 0
        if self.left_size == 0:
            median = self.right_half[0]
        if self.right_size == 0:
            median = -self.left_half[0]
        
        if self.left_size == self.right_size:
            median = (-self.left_half[0] + self.right_half[0])/2
        elif self.left_size > self.right_size:
            median = -self.left_half[0]
        else:
            median = self.right_half[0]
        # print(f"found median  : {median}")
        return median 
        


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()