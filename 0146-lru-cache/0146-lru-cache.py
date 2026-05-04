class Node:
    def __init__(self,key=0, val=0, next=None, previous=None):
        self.val = val
        self.key = key
        self.next = next
        self.previous = previous

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def insert_at_end(self, node):
        prev = self.tail.previous
        prev.next = node
        node.previous = prev

        self.tail.previous = node
        node.next = self.tail

    
    def delete(self, node):
        left = node.previous
        right = node.next
        left.next = right
        right.previous = left

        node.next = None
        node.previous = None
        return node

    def move_to_end(self, node):
        node = self.delete(node)
        self.insert_at_end(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.node_map = {}
        

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.dll.move_to_end(node)

            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.dll.move_to_end(node)
            return
        else:

            if not self.capacity:
                # delete the leftmost node (lru) fromm linkedlist
                lru_node = self.dll.delete(self.dll.head.next)
                self.node_map.pop(lru_node.key)
                self.capacity += 1

            new_node = Node(key=key, val=value)
            self.dll.insert_at_end(new_node)
            self.node_map[key] = new_node
            self.capacity -= 1 

            return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)