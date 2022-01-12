lass Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        self.inOder(root,ans)
        return ans
    
    
    def inOder(self,root,ans):
        
        if root == None:
            return
        
        
        self.inOder(root.left,ans)
        ans.append(root.val)
        self.inOder(root.right,ans)
        
        return
