from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    # Modified solution to work with LinkedList class
    def reverseKGroup(self, k: int) -> Optional[ListNode]:
        '''
        given head of linked list, reverse k nodes of the list at a time
        return the modified list
        
        k is a positive integer and <= length of the linked list
        if the number of nodes is not a multiple of k, then the leftover nodes should remain as is
        
        cannot alter the values in the list's nodes
        '''
        dummy = ListNode(0, self.head)
        kPrev = dummy
        
        while True:
            kth = self.getKth(kPrev, k)
            if not kth:
                break
            
            kNext = kth.next
            
            # reverse
            # set 1st node of group's next to 1st of next group
            prev, cur = kth.next, kPrev.next
            while cur != kNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                
            temp = kPrev.next
            kPrev.next = kth
            kPrev = temp
            
        self.head = dummy.next
                
            
    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
        
        
# head = [1,2,3,4,5], k = 2 # [2,1,4,3,5]      
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.reverseKGroup(2)
print(llist.printList())
        