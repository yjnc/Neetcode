# # Leetcode given definition for singly-linked list.
# class Node:
#     def __init__(self, key=0, val=0, next=None, prev=None):
#         self.key, self.val = key, val
#         self.prev, self.next = prev, next

# class LRUCache:
#     '''
#     Least Recently Used Cache
    
#     '''
#     def __init__(self, capacity: int):
#         '''
#         initialize LRU cache with positive size capacity
#         '''
#         self.capacity = capacity
#         self.cache = {} # key, node pointer pair
        
#         # Initialize oldest to newest sorting nodes
#         self.oldest, self.newest = Node(0, 0), Node(0,0)
#         self.oldest.next = self.newest
#         self.newest.prev = self.oldest
        
#     def remove(self, node):
#         '''
#         remove node from the doubly linked list
#         '''
#         prev, nxt = node.prev, node.next
#         prev.next = nxt
#         nxt.prev = prev
         
#     def insert(self, node):
#         '''
#         insert at the rightmost position
#         '''    
#         # previously newest node
#         right = self.newest.prev
        
#         # insert node in between prev newest node and the newest node pointer
#         right.next = self.newest.prev = node
#         node.prev, node.next = right, self.newest
        
#     def get(self, key: int) -> int:
#         '''
#         Return value of the key if key exists, else return -1
#         O(1)
#         '''
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1
        
#     def put(self, key: int, value: int) -> None:
#         '''
#         update value of key if key exists. otherwise, add key-value pair to the cache
#         if number of keys exceed capacity, evict the least recently used key
#         O(1)
#         '''
#         # if key in cache, remove it to update
#         if key in self.cache:
#             self.remove(self.cache[key])
            
#         # insert updated key value pair
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         # check if cache capacity is exceeded
#         if len(self.cache) > self.capacity:
#             del self.cache[self.oldest.next.key]
#             self.remove(self.oldest.next)
            



# Alternative Solution using OrderedDict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key:int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.move_to_end(key, False)
            return val
        return -1
    
    def put(self, key:int, value:int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()





# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1)) # 1
obj.put(3,3)
print(obj.get(2)) # -1
obj.put(4,4)
print(obj.get(1)) # -1
print(obj.get(3)) # 3
print(obj.get(4)) # 4
