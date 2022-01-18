class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSame(p,q)
        
    def isSame(self,p,q):
        
        if p == None and q == None:
            return True
        
        if p == None or q == None or p.val != q.val:
            return False
        
        return self.isSame(p.left,q.left) and self.isSame(p.right,q.right)
        
