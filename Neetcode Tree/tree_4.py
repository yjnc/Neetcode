from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        Given binary tree, determine if it is height balanced 
        (height balanced - left/right subtrees of every node differ in height by no more than 1)
        '''
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # If all preceding nodes are balanced, we get True
            balanced = (left[0] and right[0] 
                        and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]