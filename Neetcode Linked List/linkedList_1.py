from typing import Optional

# Leetcode given definition for singly-linked list.
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
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next
        
    def reverseList(self):
        '''
        Given the head of a singly linked list, reverse the list and return the reversed list
        '''
        prev, cur = None, self.head
        
        # loop until we reach end of list (ie. cur = None)
        while cur:
            # swap next node as current node and current node as next node's new next node
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        self.head = prev





# linkedList = [1,2,3,4,5] # [5,4,3,2,1]
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

llist.reverseList()
llist.printList()