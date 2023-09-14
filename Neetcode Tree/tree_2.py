from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Given the root of a binary tree, return its maximum depth (longest path from root to farthest leaf node)
        '''
        # Recursive DFS Solution
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
       
       
       
        # BFS Solution (inefficient for scenario)
        nodes = deque()
        if root:
            nodes.append(root)
            
        depth = 0   
        # note: a while loop checks the condition at the start of each loop and will not terminate mid-loop unless directed to do so
        while nodes:
            for i in range(len(nodes)):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            depth += 1
        return depth
    
    
        # Stack Solution
        stack = [[root, 1]]
        depth = 0
        
        while stack:
            node, level = stack.pop()
            if node:
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
                depth = max(depth, level)
        return depth
        

        
# root = [] # 0
# root = [3,9,20,null,null,15,7] # 3