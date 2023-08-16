from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        '''
        Given heads of two sorted linked lists, list1, list2
        merge two lists into one sorted list
        return head of the merged linked list
        '''
        nodeA, nodeB = list1, list2
        
        # takes care of edge cases where list is empty
        temp = ListNode()
        cur = temp
            
        # loop until we reach end of list for either list
        while nodeA and nodeB:
            # make the smaller node the next node
            if nodeA.val <= nodeB.val:
                cur.next = nodeA
                nodeA = nodeA.next 
            else:
                cur.next = nodeB
                nodeB = nodeB.next
            cur = cur.next
        
        # if one of the list still has nodes, make it the next node
        if nodeA:
            cur.next = nodeA
        elif nodeB:
            cur.next = nodeB

        return temp.next
    
    
# list1, list2 = [1,2,4], [1,3,4] # [1,2,3,4,4]
# list1, list2 = [], [] # []
# list1, list2 = [], [0]