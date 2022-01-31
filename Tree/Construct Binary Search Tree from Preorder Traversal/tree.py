class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        inorder = sorted(preorder)
        # processing map for better time comp.
        preIndx = [0]
        memo = {}
        lenInorder = len(inorder)
        for indx in range(lenInorder):
            memo[inorder[indx]] = indx
            
        return self.constructTree(preorder,memo,0,lenInorder-1,preIndx)
    
        """
        self.preIndx = 0
        return self.buildTree(preorder,1001)
    
    def buildTree(self,preorder,boundVal):
        
        if self.preIndx >= len(preorder) or preorder[self.preIndx] >= boundVal:
            return None
        
        root = TreeNode(preorder[self.preIndx])
        self.preIndx += 1
        
        root.left = self.buildTree(preorder,root.val)
        root.right = self.buildTree(preorder,boundVal)
        
        return root
    
        
    
        
    def constructTree(self,preorder,memo,start,end,preIndx):
        
        if start > end:
            return None
        
        root = TreeNode(preorder[preIndx[0]])
        current = memo[preorder[preIndx[0]]]
        preIndx[0] += 1
        
        root.left = self.constructTree(preorder,memo,start,current-1,preIndx)
        root.right = self.constructTree(preorder,memo,current+1,end,preIndx)
        
        return root
        
