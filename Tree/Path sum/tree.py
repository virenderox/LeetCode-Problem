# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        return self.isPossible(root,target,0)
    
    
    def isPossible(self,root,target,currentSum):
        
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return currentSum + root.val == target
        
        
        return self.isPossible(root.left,target,currentSum + root.val) or self.isPossible(root.right,target,currentSum + root.val)
