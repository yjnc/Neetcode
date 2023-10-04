from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        '''
        Given root of BST, return level order traversal of its nodes' values (ie. BFS)
        '''
        # Binary Search Tree Structure
        bst = []
        # Queue
        q = []
        
        # Initialize queue: add root
        if root:
            q.append(root)
            
        while q:
            # store cur level node values
            cur = []
            
            for i in range(len(q)):
                node = q.pop(0)
                cur.append(node.val)
                
                # add cur nodes neighbors to queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # add cur level node values to binary tree
            bst.append(cur)
        
        return bst
                