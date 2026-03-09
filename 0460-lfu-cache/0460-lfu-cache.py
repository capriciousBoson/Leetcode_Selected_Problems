class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

        
    
    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        next_node.prev = prev_node
        prev_node.next = next_node

        node.next = None
        node.prev = None
        self.length -= 1
        
        return node

    def delete_front_node(self):
        node = self.head.next
        self.head.next = self.head.next.next
        node.next.prev = self.head
        node.next = None
        node.prev = None
        self.length -= 1
        return node

    
    def insert_at_end(self, node):
       
        node.next = self.tail
        node.prev = self.tail.prev

        node.next.prev = node
        node.prev.next = node
        self.length += 1

        return node


    def move_to_end(self,node):
        deleted_node = self.delete(node)
        self.insert_at_end(deleted_node)
    
    def show(self):
        curr = self.head
        print(f"head : -------------------------------------")
        while curr:
            print(curr.val)
            curr = curr.next
        print(f"tail :---------------------------------------")



class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.nodeMap = {}
        self.freqMap = {} 
        self.minFreq = float('inf')
    
    def _increaseKeyFreq(self, key):

        keyFreq = self.freq[key]

        dll = self.freqMap[keyFreq]
        node = self.nodeMap[key]
        dll.delete(node)

        self.freq[key] += 1
        if self.freq[key] not in self.freqMap : 
            self.freqMap[self.freq[key]] = DoublyLinkedList()

        new_dll = self.freqMap[self.freq[key]]
        new_dll.insert_at_end(node)

        if dll.length == 0:
            self.freqMap.pop(keyFreq)
            if keyFreq == self.minFreq:
                self.minFreq += 1
    
    def _deleteLfuLru(self):
        minFreqDll = self.freqMap[self.minFreq]
        deletedNode  = minFreqDll.delete_front_node()
        deletedKey = deletedNode.key
        self.cache.pop(deletedKey)
        self.nodeMap.pop(deletedKey)
        self.freq.pop(deletedKey)

        if minFreqDll.length == 0:
            self.freqMap.pop(self.minFreq)
            # self.minFreq += 1
        self.capacity += 1
        return


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._increaseKeyFreq(key)

        return self.cache[key]

        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key] = value
            self._increaseKeyFreq(key)

        else:
            if self.capacity == 0:
                self._deleteLfuLru()

            self.cache[key] = value
            self.freq[key] = 1
            if self.freq[key] not in self.freqMap:
                self.freqMap[self.freq[key]] = DoublyLinkedList()

            dll = self.freqMap[self.freq[key]]
            node = Node(key, value)
            dll.insert_at_end(node)
            self.nodeMap[key] = node
            self.capacity -= 1
            self.minFreq = min(self.minFreq, self.freq[key])




        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)