from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Personally created LinkedList class with leetcode problem function, reverseList
class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        
    def append(self, val):
        node = ListNode(val)
        cur = self.head
        
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.head = node    
    
    def printList(self):
        llist = []
        cur = self.head
        while cur:
            llist.append(cur.val)
            cur = cur.next       
          
        return llist
            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Given head of linked list, remove the nth node from the end of the list and return its head
        (Modified answer to be runnable on visual studio code with the class functions)
        '''
        # dummy node exists before the head node as a placeholder
        # this allows for edge case [1], n = 1
        dummy = ListNode(0, head)
        l, r = dummy, head
        
        # Offset r pointer by n from l pointer
        while n > 0:
            r = r.next
            n -= 1
        
        # Loop until r pointer reaches the end of list
        while r:
            r = r.next
            l = l.next
        
        # Delete nth node from the end
        l.next = l.next.next
        self.head = dummy.next
        
        
        # # Alternative Solution using a counter
        # cur = head
        # count = 0
        # while cur:
        #     count += 1
        #     cur = cur.next
            
        # prev, cur = None, head
        # while cur:
        #     if count == n:
        #         nextNode = cur.next
        #         if prev == None:
        #             self.head = nextNode
        #         else:
        #             prev.next = nextNode
        #         return self.head
            
        #     count -= 1
        #     prev = cur
        #     cur = cur.next
            
        


llist = LinkedList()

# # head= [1,2,3,4,5] n = 2 # [1,2,3,5]
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# n = 2

# head = [1], n = 1 # []
llist.append(1)
n = 1

# # head = [1,2], n = 1 # [1]
# llist.append(1)
# llist.append(2)
# n = 1


llist.removeNthFromEnd(llist.head, n)
print("result:", llist.printList())
