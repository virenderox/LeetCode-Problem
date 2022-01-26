class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        self.Sum(root,low,high,ans)
        return sum(ans)
    
    def Sum(self,root,low,high,ans):
        
        if root == None:
            return 
        
        if root.val >= low and root.val <= high:
            ans.append(root.val)
            
        self.Sum(root.left,low,high,ans)
        self.Sum(root.right,low,high,ans)

        return
    
