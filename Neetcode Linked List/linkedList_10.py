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
    
    
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Given array of k linked lists, lists, sorted in ascending order
        Merge all the linked lists into one sorted linked list and return
        '''
        # edge case
        if not lists or len(lists) == 0:
            return None
        
        # merge lists in pairs until there's only one list remaining
        # O(nlogk) -> O(n) merging performed logk times -> number of times we take k lists and divide by two (ie. merge two into one list)
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.merger(l1, l2))
            lists = mergedList
        return lists[0]
    
    
    def merger(self, l1: ListNode, l2: ListNode):
        # O(n) 
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
                
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
                
        
        

# lists = [[1,4,5],[1,3,4],[2,6]] # [1,1,2,3,4,4,5,6]
l1 = LinkedList()
l1.append(1)
l1.append(4)
l1.append(5)

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)

l3 = LinkedList()
l3.append(2)
l3.append(6)

lists = [l1.head, l2.head, l3.head]

solution = Solution()
print(solution.mergeKLists(lists))
