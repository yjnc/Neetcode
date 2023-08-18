from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
           
           
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Given two non-empty linked lists representing two non-negative integers
        digits stored in reverse order, each node contains single digit
        return the sum of the two numbers as a linked list
        (May assume two number do not contian any leading zero except number 0)
        '''
        # Solution O(n)
        prev = None
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # break down the sum into tenth and ones place (note: b/c max digit is 9, sum will not exceed tenth place)
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
              
            sumNode = ListNode(digit)  
            
            # for handling when at the head of the list
            if prev == None:
                head = sumNode
            else:
                prev.next = sumNode
            prev = sumNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head
    
    
        # Alternative O(n) solution using dummy node
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            cur.next = ListNode(digit)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
# l1 = [2,4,3], l2 = [5,6,4] # [7,0,8]
# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] # [8,9,9,9,0,0,0,1]