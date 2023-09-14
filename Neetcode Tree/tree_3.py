from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Given the root of binary tree, return the diameter of the tree
        (diameter - length of the longest path between any two nodes in a tree, may or may not pass though the root)
        '''
        # O(n) Solution
        
        # Use a list to optimize memory bc python makes a copy of the primitive types
        # everytime it is run through a function
        diam = [0]
        
        def dfs(root):
            nonlocal diam
            
            # Edge case: empty tree
            if not root:
                return -1
            
            # Height of left & right trees
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Calculate diameter
            diam[0] = max(2 + left + right, diam[0])
            
            # Return height
            # Add 1 to account for the node itself when calc height
            return 1 + max(left, right)
        
        dfs(root)
        return diam[0]