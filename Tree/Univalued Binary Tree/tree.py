# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        check = root.val
        return self.isUnique(root,check)
    
    
    def isUnique(self,root,check):
        
        if root == None:
            #print("hy")
            return True
        
        #print(root.val,check)
        
        if root.val != check:
            #print("hy")
            return False
        
        l = self.isUnique(root.left,check)
        
        r = self.isUnique(root.right,check)
        
        return l and r
        
            
        
