# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Given BST, return the LCA node of two given nodes
        Lowest common ancestor - b/t two nodes p, q, it's the lowest node in tree T that has both p and q as descendents (node can be descendant of itself)
        '''
        # Given that a binary tree's left is < root and right is > root, we can use the following logic
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # if it is neither, then the two nodes are in either sides of the node, making it the LCA
            else:
                return root 