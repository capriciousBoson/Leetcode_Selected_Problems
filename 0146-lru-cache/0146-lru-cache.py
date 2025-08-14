class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cache = {}
        self.current_capacity = 0
        self.lru = {}
        self.time = 0

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.time += 1
            self.lru[key] = self.time
            return self.cache[key]
            
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.time += 1

        if key in self.cache:
            self.cache[key] = value
            self.lru[key] = self.time
        else:
            if self.current_capacity == self.max_capacity:

                lru_key = min(self.lru, key=self.lru.get)
                del self.lru[lru_key]
                del self.cache[lru_key]
                self.current_capacity -= 1
                
            self.cache[key] = value
            self.current_capacity += 1
            self.lru[key] = self.time
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)