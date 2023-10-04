class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        '''
        Given root of two bst root, subroot, return True if there is a subtree of root with the same structure and node values of subRoot, else False.
        '''
        # Check if subtree is the same
        def isSameTree(node: TreeNode, subNode: TreeNode) -> bool:
            if not node and not subNode:
                return True
            # If current node is the same, check the neighbors
            if node and subNode and node.val == subNode.val:
                return isSameTree(node.left, subNode.left) and isSameTree(node.right, subNode.right)
            return False
        
        # Edge Cases:
        # If subTree is empty
        if not subRoot:
           return True
        # If tree is empty
        if not root:
            return False
        
        # Check if current node + its children are the same, if not...
        if isSameTree(root, subRoot):
            return True
        # Check if subtree on one of root's child nodes
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
        
        
        
             