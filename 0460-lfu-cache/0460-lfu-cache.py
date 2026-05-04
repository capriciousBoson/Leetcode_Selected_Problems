class Node:
    def __init__(self, key=0, val=0, next=None, previous=None):
        self.key = key
        self.val = val
        self.next = next
        self.previous = previous

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.length = 0
    
    def insert_at_end(self, node):
        prev = self.tail.previous
        prev.next = node
        node.previous = prev

        self.tail.previous = node
        node.next = self.tail
        self.length += 1
    
    def delete(self, node):
        left = node.previous
        right = node.next
        left.next = right
        right.previous = left

        node.previous = None
        node.next = None

        self.length -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency_dlls = {}
        self.freq_map = {}
        self.node_map = {}
        self.min_freq = float('inf')

    
    def _increase_key_frequency(self, key):
        node = self.node_map[key]
        f = self.freq_map[key]
        dll = self.frequency_dlls[f]
        # remove the node from dll of frequency f
        dll.delete(node)

        # increase key frequency and add the dll of new inreased frequency
        self.freq_map[key] += 1
        if self.freq_map[key] not in self.frequency_dlls:
            self.frequency_dlls[self.freq_map[key]] = DoublyLinkedList()
        self.frequency_dlls[self.freq_map[key]].insert_at_end(node)

        # cleanup
        if dll.length == 0:
            self.frequency_dlls.pop(f)
            if f==self.min_freq:
                self.min_freq += 1
        return 

    def _delete_lfu_lru(self):
        dll = self.frequency_dlls[self.min_freq]
        deleted_node = dll.delete(dll.head.next)

        self.node_map.pop(deleted_node.key)
        self.freq_map.pop(deleted_node.key)
        self.capacity += 1

        # cleanup
        if dll.length==0:
            self.frequency_dlls.pop(self.min_freq)
        return



    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self._increase_key_frequency(key)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in  self.node_map:
            if not self.capacity:
                self._delete_lfu_lru()
            
            new_node = Node(key=key, val=value)
            self.freq_map[key] = 1
            self.min_freq = min(self.min_freq, self.freq_map[key])

            if self.freq_map[key] not in self.frequency_dlls:
                self.frequency_dlls[self.freq_map[key]] = DoublyLinkedList()
            
            dll = self.frequency_dlls[self.freq_map[key]]
            dll.insert_at_end(new_node)
            self.node_map[key] = new_node
            self.capacity -= 1

        else:
            node = self.node_map[key]
            node.val = value
            self._increase_key_frequency(key)



             
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)