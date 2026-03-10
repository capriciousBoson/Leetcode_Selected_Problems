class MyCalendar:

    def __init__(self):
        self.intervals = []
        # self.start_times = {}
        # self.end_times = {}

        

    def book(self, startTime: int, endTime: int) -> bool:

        # if startTime in self.start_times or endTime in self.end_times:
        #     return False
        # print(f"\nalready booked : {self.intervals}")
        # print(f"new interval : {[startTime, endTime]}")
        
        for interval in self.intervals:
            if interval[0] <= startTime <interval[1]:
                # print(f"conflict with : {interval}")
                return False
            if interval[0] < endTime <=interval[1] : 
                # print(f"conflict with : {interval}")
                return False

            if startTime <= interval[0] and endTime >= interval[1]:
                # print(f"conflict with : {interval}")
                return False
    
        # print(f"no conflict ---")
        i = len(self.intervals)
        self.intervals.append([startTime, endTime])
        # self.start_times[startTime] = i
        # self.end_times[endTime] = i
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)