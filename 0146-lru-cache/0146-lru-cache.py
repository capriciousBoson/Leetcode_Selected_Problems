class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        
    
    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        next_node.prev = prev_node
        prev_node.next = next_node

        node.next = None
        node.prev = None
        
        return node

    def delete_front_node(self):
        node = self.head.next
        self.head.next = self.head.next.next
        node.next.prev = self.head
        node.next = None
        node.prev = None
        return node

    
    def insert_at_end(self, node):
       
        node.next = self.tail
        node.prev = self.tail.prev

        node.next.prev = node
        node.prev.next = node

        return node


    def move_to_end(self,node):
        deleted_node = self.delete(node)
        self.insert_at_end(deleted_node)
    
    def show(self):
        curr = self.head
        # print(f"head : -------------------------------------")
        while curr:
            # print(curr.val)
            curr = curr.next
        # print(f"tail :---------------------------------------")
        



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.node_map = {}
        self.key_map = {}
    


    def get(self, key: int) -> int:
        # print(f"\nGET : key : {key} -----------------------")

        if key in self.node_map:
            node = self.node_map[key]
            self.dll.move_to_end(node)
            # print(f"found key, val  :{key, node.val}")
            return node.val
        else:
            # print(f"couldnot find key :{key}")
            return -1
    


    def put(self, key: int, value: int) -> None:
        # print(f"\nPUT call for  key,val : {key,value} ----")
        # self.dll.show()

        if key not in self.node_map: #insert a new node
            # print(f"inserting a new node with key,val : {key,value} --------")    

            if not self.capacity:
                # print(f"capacity reached : {self.capacity}")
                deleted_node = self.dll.delete_front_node()
                # print(f"after deletiong front : ")
                self.dll.show()
                # print(f"head :{self.dll.head.val} | tail : {self.dll.tail.val}")
                # print(f"deletd front node : {deleted_node.val}")
                deleted_key = self.key_map[deleted_node]
                # print(f"deleted key, val : {deleted_key, deleted_node.val}")

                self.node_map.pop(deleted_key)
                self.key_map.pop(deleted_node)
                self.capacity += 1

            node = Node(value)
            self.node_map[key] = node
            self.key_map[node] = key
            self.dll.insert_at_end(node)
            # print(f"inserted new node with key, val :  {key, value}")
            # self.dll.show()
            # print(f"node_map : {self.node_map}")
            # print(f"key_map : {self.key_map}")
            self.capacity -= 1
            # print(f"capacity : {self.capacity}")
        else:                       #update existing node
            node = self.node_map[key]
            node.val = value
            self.dll.move_to_end(node)

        return



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)