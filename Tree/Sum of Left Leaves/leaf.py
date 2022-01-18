# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        return self.sumOfLeftLeave(root,False)
    
    def sumOfLeftLeave(self,root,isLeft):
        
        if root is None:
            return 0
        
        if root.left is None and root.right is  None and isLeft is True:
            return root.val
        
        left = self.sumOfLeftLeave(root.left,True)
        right = self.sumOfLeftLeave(root.right,False)
        
        return left + right
        
