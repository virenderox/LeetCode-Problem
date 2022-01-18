"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import LifoQueue
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        stack = LifoQueue()
        self.postOrderIterative(root,ans,stack)
        #self.postOder(root,ans)
        return reversed(ans)
    
    def postOrderIterative(self,root,ans,stack):
        
        if root == None:
            return
        
        stack.put(root)
        while not(stack.empty()):
            current = stack.get()
            ans.append(current.val)
            
            for child in current.children:
                
                if child != None:
                    stack.put(child)
                
        
        return ans
    
    
    def postOder(self,root,ans):
        
        if root == None:
            return
        
        
        for child in root.children:
            self.postOder(child,ans)
        ans.append(root.val)
        
        return
        
