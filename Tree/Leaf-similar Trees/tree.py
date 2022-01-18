# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        self.isLeafSame(root1,l1)
        self.isLeafSame(root2,l2)
        return l1 == l2
        
        
    def isLeafSame(self,root,l):
        
        if root == None:
            return None
        
        if root.left == None and root.right == None:
            l.append(str(root.val))
            return
        
       # if root1.right == None and root2.right == None:
            
            #return root1.val == root2.val
        
        self.isLeafSame(root.left,l)
        self.isLeafSame(root.right,l)
        
        return
        
        
