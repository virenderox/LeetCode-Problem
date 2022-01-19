class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.isSame(root.left,root.right)
    
    
    def isSame(self,rootLeft,rootRight):
        
        if rootLeft == None and rootRight == None:
            return True
        
        if rootLeft == None or rootRight == None or rootLeft.val != rootRight.val:
            return False
        
        
        return self.isSame(rootLeft.left,rootRight.right) and self.isSame(rootLeft.right,rootRight.left)
        
        
