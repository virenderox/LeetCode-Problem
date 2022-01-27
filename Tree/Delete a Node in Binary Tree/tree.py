# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root == None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
            
        else:
            if root.left == None and root.right == None:
                root = None
                return root
            
            if root.left != None and root.right == None:
                root = root.left
                return root
            
            if root.right != None and root.left == None:
                root = root.right
                return root
            
            rightSubTree = self.findLeft(root.right)
            tmp = root.val
            root.val = rightSubTree.val
            rightSubtree = tmp
            
            root.right = self.deleteNode(root.right,rightSubTree.val)
            
            return root
        return root
    
    def findLeft(self,root):
        
        while root.left != None:
            root = root.left
        
        return root
            
            
