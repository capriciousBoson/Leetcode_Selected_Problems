class MyCalendar:

    def __init__(self):
        self.intervals = []


        

    def book(self, startTime: int, endTime: int) -> bool:
        # print(f"\nnew interval : {[startTime, endTime]}")
        # print(f"current intervals : {self.intervals}")
        idx =  bisect.bisect_left(self.intervals, [startTime, endTime])

        # print(f"bisect left : {idx} ")

        if idx-1 >= 0:
            previous_event = self.intervals[idx-1]
            if previous_event[0] <= startTime < previous_event[1]:
                return False

        if idx < len(self.intervals):
            next_event = self.intervals[idx]
            if next_event[0] < endTime :
                return False
            
            
        
        bisect.insort(self.intervals, [startTime, endTime])
        return True




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)