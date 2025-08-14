from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cache = OrderedDict()
        self.current_capacity = 0


        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
            
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if self.current_capacity == self.max_capacity:
                self.cache.popitem(last=False)
                self.current_capacity -= 1
       
            self.cache[key] = value
            self.cache.move_to_end(key)
            self.current_capacity += 1

            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)