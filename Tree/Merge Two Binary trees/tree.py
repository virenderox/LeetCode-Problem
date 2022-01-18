# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.merge(root1,root2)
    
    def merge(self,root1,root2):
        
        if root1 == None and root2 == None:
            return None
        
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        
        newNode = TreeNode(root1.val + root2.val)
        
        newNode.left = self.merge(root1.left,root2.left)
        newNode.right = self.merge(root1.right,root2.right)
        
        return newNode
        
