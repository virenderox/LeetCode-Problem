# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        """
        Extra space required here
        ans = []
        self.inOrder(root,ans)
        lenAns = len(ans)
        for i in range(1,lenAns):
            if ans[i-1] >= ans[i]:
                return False
            
        return True
        
        can be do in one travsal and constant space
        """
        
        self.prevVal = float("-inf")
        return self.isBST(root)
    
    def isBST(self,root):
        
        if root is None:
            return True
        
        leftAns = self.isBST(root.left)
        
        if root.val <= self.prevVal:
            return False
        self.prevVal = root.val
        
        
        rightAns = self.isBST(root.right)
        return leftAns and rightAns
        
        
        
    def inOrder(self,root,ans):
        
        if root == None:
            return 
        
        self.inOrder(root.left,ans)
        ans.append(root.val)
        self.inOrder(root.right,ans)
        
    
        return
        
        
        
        
