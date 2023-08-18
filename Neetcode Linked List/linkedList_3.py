from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Given head of singly linked-list L0 -> L1 -> ... -> Ln-1 -> Ln
        Reorder list to be: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
        Do not return anything, modify head in-place instead.
        '''
        
        # O(n) solution
        # Find the middle of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
           
        # Reverse the order of the second half of the linked list    
        nodeB = slow.next
        prev = slow.next = None
        while nodeB:
            # store next node before modifying
            temp = nodeB.next
            
            # reverse the order
            nodeB.next = prev
            prev = nodeB
            nodeB = temp
        
        # Merge / Reorder list
        nodeA, nodeB = head, prev
        while nodeB:
            # store next node before modifying
            tempA, tempB = nodeA.next, nodeB.next
            
            # merge
            nodeA.next = nodeB
            nodeB.next = tempA
            
            # update pointers to next node
            nodeA, nodeB = tempA, tempB
        
        
        
        # Less memory efficient solution
        # move linked list to an array format
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
            
        # reorder the array into desired order
        reorderArr = []
        l, r = 0, len(arr) - 1
        while l <= r:
            reorderArr.append(arr[l])
            reorderArr.append(arr[r])
            l += 1
            r -= 1
        
        # modify the linked list using the reordered array
        cur = head
        for i in range(1, len(reorderArr)):
            cur.next = reorderArr[i]
            cur = cur.next
            