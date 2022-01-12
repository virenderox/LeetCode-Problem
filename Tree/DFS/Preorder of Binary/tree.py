class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        self.preOder(root,ans)
        return ans
    
    
    def preOder(self,root,ans):
        
        if root == None:
            return
        
        ans.append(root.val)
        self.preOder(root.left,ans)
        self.preOder(root.right,ans)
        
        return
