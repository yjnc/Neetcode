from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
# Personally created LinkedList class with leetcode problem function, reverseList
class LinkedList:
    def __init__(self, head=None, length=0) -> None:
        self.head = head
        self.length = length
        
    def append(self, val):
        node = ListNode(val)
        cur = self.head
        
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.head = node   
            
        self.length += 1 
    
    def printList(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
            
    def createCycle(self, pos: int):
        '''
        Creates a cycle at the given position
        
        *Assumes pos is always a positive integer
        '''        
        # for when pos is negative, convert it to the positive index
        if pos < 0:
            pos = self.length + pos
        
        # if pos is 0 and the list only has one node,
        # it is not considered a cycle with one node pointing back to itself
        if pos == 0 and self.length == 1:
            return False
        
        # loop until we reach the node in position to create cycle
        cur = self.head
        for i in  range(1, pos + 1):
            cur = cur.next
            
        kthNode = cur
        
        # adjust node's next pointer to be at the given position
        while cur.next:
            cur = cur.next
        cur.next = kthNode
        
        
            
            
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Given head (head of linked list), determine if list has a cycle
        return true if there is a cycle, else false.
        
        Cycle:
            - some node in list can be reached again by continuously following the next pointer
            - internally, pos is used to denote the index of node that tail's next pointer is connected to
            - pos is NOT passed as a param
        '''
        
        # Floyd's Tortoise & Hare Algorithm O(n)
        fast = head
        
        # Checking fast & fast.next to ensure it hasn't reached the end already
        while fast and fast.next:
            # slow pointer (head) moves by one, fast pointer moves by two
            head = head.next
            fast = fast.next.next
            
            # slow and fast pointer will only meet if there is a cycle
            # as fast pointer slowly closes the gap between the slow pointer
            if head == fast:
                return True
            
        return False
        
        
        
# head = [3,2,0,-4], pos = 1 # True
llist = LinkedList()
llist.append(3)
llist.append(2)
llist.append(0)
llist.append(-4)
llist.createCycle(1)

# head = [1,2], pos = 0 # True
llist.append(1)
llist.append(2)
llist.createCycle(0)

# head = [1], pos = 0 # False
llist.append(1)
llist.createCycle(-1)

solution = Solution()
print(solution.hasCycle(llist.head))