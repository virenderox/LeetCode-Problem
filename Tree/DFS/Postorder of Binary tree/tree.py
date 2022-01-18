# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import LifoQueue
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = LifoQueue()
        self.postOrderIterative(root,ans,stack)
        #self.postOder(root,ans)
        return ans
    
    def postOrderIterative(self,root,ans,stack):
        
        if root == None:
            return ans
        
        stack.put(root)
        while not(stack.empty()):
            current = stack.get()
           # print(current)
            
            ans.append(current.val)
            if current.left != None:
                stack.put(current.left)
                
            if current.right != None:
                stack.put(current.right)
                
            
                
        
        return ans.reverse()
    
    
    def postOder(self,root,ans):
        
        if root == None:
            return
        
        
        self.postOder(root.left,ans)
        
        self.postOder(root.right,ans)
        ans.append(root.val)
        
        return
