class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    # and a head, tail and capacity 
    def __init__(self, capacity: int):
        # which stores the (key value) pairs as key and node reference 
        self.cacheMap={}
        self.capacity=capacity 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next=self.tail
        self.tail.prev=self.head

    
    def get(self, key: int) -> int:
        if key not in self.cacheMap:
            return -1
        # getting the node reference 
        node=self.cacheMap[key]
        self._remove(node)
        self._insertAfterHead(node)
        return node.value       

    # if the key is already present replace the connection !!!!!!!!!
    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            # getting the reference 
            node=self.cacheMap[key]
            node.value=value
            self._remove(node)
            self._insertAfterHead(node)
        else:
            #we need to make separate connection between head and tail
            # check the length first
            if len(self.cacheMap)==self.capacity:
                # need to remove the tail connection, lru is the address here or the value of the hashmap
                lru=self.tail.prev
                self._remove(lru)
                # we need to remove the connection or reference as well !
                # self.cacheMap[lru.key] = None 
                # deleting the node 
                del self.cacheMap[lru.key]
            # now create a new node and start connecting after the head 
            new_node=Node(key,value)
            self.cacheMap[key]=new_node
            self._insertAfterHead(new_node)

    # remove the connection
    # head and tail are dummy nodes Real nodes are in between
    # delete or remove a node by cutting off the links 
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # add the connection after the head 
    def _insertAfterHead(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        


# # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) 