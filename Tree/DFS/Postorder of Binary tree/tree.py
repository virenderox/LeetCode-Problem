class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        self.postOder(root,ans)
        return ans
    
    
    def postOder(self,root,ans):
        
        if root == None:
            return
        
        
        self.postOder(root.left,ans)
        
        self.postOder(root.right,ans)
        ans.append(root.val)
        
        return
