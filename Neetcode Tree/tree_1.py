from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    def __init__(self, root=None):
        self.root = root      
        
    def append(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.appendHelper(val, self.root)
            
    def appendHelper(self, val, node):
        if val < node.val:
            if node.left:
                self.appendHelper(val, node.left)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self.appendHelper(val, node.right)
            else:
                node.right = TreeNode(val)       
    
    def printTree(self, node):
        '''
        prints left node, then root, and then right node
        '''
        if node.left:
            self.printTree(node.left)
        print(node.val),
        if node.right:
            self.printTree(node.right)     
        

    def invertTree(self, root) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
    
        
        # Alternative Condensed Solution
        if not root: 
            return None
        else:
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            
            
tree = Tree()
tree.append(4)
tree.append(2)
tree.append(7)
tree.append(1)
tree.append(3)
tree.append(6)
tree.append(9)
print("Original Tree")
tree.printTree(tree.root)
tree.invertTree(tree.root)
print("Inverted Tree")
tree.printTree(tree.root)