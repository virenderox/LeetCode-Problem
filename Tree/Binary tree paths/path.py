# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        self.rootToLeaf(root,"",ans)
        return ans
    
    def rootToLeaf(self,root,currentPath,ans):
        
        if root == None:
            return
        
        
        if root.left == None and root.right == None:
            currentPath += str(root.val)
            ans.append(currentPath)
            return 
        
        currentPath += str(root.val) + "->"
        
        self.rootToLeaf(root.left,currentPath,ans)
        self.rootToLeaf(root.right,currentPath,ans)
        
        return
            
