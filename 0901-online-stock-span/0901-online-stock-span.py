class StockSpanner:

    def __init__(self):
        self.price_history = []
        self.monotonic_stck = [-1]

    def next(self, price: int) -> int:
        self.price_history.append(price)

        while self.monotonic_stck[-1]!= -1 and price >= self.price_history[self.monotonic_stck[-1]]:
            self.monotonic_stck.pop()

        last_idx = self.monotonic_stck[-1]
        curr_idx = len(self.price_history)-1

        self.monotonic_stck.append(curr_idx)
        return curr_idx - last_idx


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)