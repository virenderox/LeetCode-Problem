class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # processing map for better time comp.
        preIndx = [0]
        memo = {}
        lenInorder = len(inorder)
        for indx in range(lenInorder):
            memo[inorder[indx]] = indx
            
        return self.constructTree(preorder,memo,0,lenInorder-1,preIndx)
    
    def constructTree(self,preorder,memo,start,end,preIndx):
        
        if start > end:
            return None
        
        root = TreeNode(preorder[preIndx[0]])
        current = memo[preorder[preIndx[0]]]
        preIndx[0] += 1
        
        root.left = self.constructTree(preorder,memo,start,current-1,preIndx)
        root.right = self.constructTree(preorder,memo,current+1,end,preIndx)
        
        return root
        
        
        
