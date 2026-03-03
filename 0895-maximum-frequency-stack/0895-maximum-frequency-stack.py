class FreqStack:

    def __init__(self):
        self.stack = []
        self.occurence = 0
        self.freq = collections.defaultdict(int)
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.occurence -= 1
        heapq.heappush(self.stack, [-self.freq[val], self.occurence, val])

    def pop(self) -> int:
        val = heapq.heappop(self.stack)[2]
        self.freq[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()