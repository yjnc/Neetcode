from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Given roots of two binary trees p, q, check if they are the same
        (same -> structurally identical with same node values)
        '''
        
        # Recursion
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
        
        # Alternative (only catches differences at the end)
        def treeHelper(node, nodes):
            if not node:
                nodes.append("None")
                return
            
            nodes.append(node.val)
            helper(node.left, nodes)
            helper(node.right, nodes)
            
        pNodes = []
        qNodes = []
        
        helper(p, pNodes)
        helper(q, qNodes)
        
        if pNodes == qNodes:
            return True
        else:
            return False