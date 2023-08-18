from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        linked list of length n, each node contains additional random pointer which can point to any node in the list or null
        construct deep copy of the list
            - exactly n new nodes where each node has its value equal to corresponding node
            - next, and random pointer should point to corresponding new nodes
            - none of the pointers in the new list should point to nodes in old list
        return the head of the copied linked list
        '''
        # Solution O(n)
        # make a copy of each node with just the value
        copiedNodes = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            copiedNodes[cur] = copy
            cur = cur.next
            
        # establish links between nodes    
        cur = head
        while cur:
            copy = copiedNodes[cur]
            copy.next = copiedNodes[cur.next]
            copy.random = copiedNodes[cur.random]
            cur = cur.next
            
        return copiedNodes[head]
            



# head = [[7,null],[13,0],[11,4],[10,2],[1,0]] # [[7,null],[13,0],[11,4],[10,2],[1,0]]