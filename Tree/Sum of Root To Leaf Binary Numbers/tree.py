# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = [0]
       # ans[0] = 0
        self.sumRoot(root,"",ans)
        return ans[0]
    
    def sumRoot(self,root,char,ans):
        
        
        if root.left == None and root.right == None:
            char += str(root.val)
            ans[0] += int(char,2)
            return
        
        if root.left != None:
            self.sumRoot(root.left,char + str(root.val),ans)
            
        if root.right != None:
            self.sumRoot(root.right,char + str(root.val),ans)
            
        return 
        
        
