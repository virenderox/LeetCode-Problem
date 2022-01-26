class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        
        ans = []
        
        self.Inoder(root,ans)
        
        dummy = newRoot =  TreeNode(-1)
        
        for val in ans:
            dummy.right = TreeNode(val)
            dummy = dummy.right
            
        return newRoot.right
         
        
        
    def Inoder(self,root,ans):
        
        if root == None:
            return None
        
        
        self.Inoder(root.left,ans)
        ans.append(root.val)
        self.Inoder(root.right,ans)
        
        return 
