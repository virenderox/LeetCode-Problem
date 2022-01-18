# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import LifoQueue
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        stack = LifoQueue()
        
        self.preOrderIterative(root,ans,stack)
        # this is recursive way self.preOderRecursive(root,ans)
        return ans
    
    
    def preOderRecursive(self,root,ans):
        
        if root == None:
            return
        
        ans.append(root.val)
        self.preOder(root.left,ans)
        self.preOder(root.right,ans)
        
        return
    
    def preOrderIterative(self,root,ans,stack):
        
        if root == None:
            return ans
        
        stack.put(root)
        while not(stack.empty()):
            current = stack.get()
           # print(current)
            ans.append(current.val)
            
            if current.right != None:
                stack.put(current.right)
                
            if current.left != None:
                stack.put(current.left)
                
        
        return ans
        
        
