# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import LifoQueue
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        stack = LifoQueue()
        self.InorderOrderIterative(root,ans,stack)
        #self.inOder(root,ans)
        return ans
    
    
    def InorderOrderIterative(self,root,ans,stack):
        
        if root == None:
            return ans
        
        self.addLeftSubtree(root,stack)
        
        while not(stack.empty()):
            current = stack.get()
           # print(current)
            ans.append(current.val)
            
            if current.right != None:
                self.addLeftSubtree(current.right,stack)
    
        return ans
    
    def addLeftSubtree(self,current,stack):
        
        stack.put(current)
        while current.left != None:
            stack.put(current.left)
            
            current = current.left
            
        return 
        
        
        
    def inOder(self,root,ans):
        
        if root == None:
            return
        
        
        self.inOder(root.left,ans)
        ans.append(root.val)
        self.inOder(root.right,ans)
        
        return
