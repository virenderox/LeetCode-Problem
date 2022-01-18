"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import LifoQueue
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        stack = LifoQueue()
        ans = []
        
        self.preOrderIterative(root,ans,stack)
        
        #self.preOderRecursive(root,ans)
        return ans
    
    def preOrderIterative(self,root,ans,stack):
        
        if root == None:
            return
        
        stack.put(root)
        while not(stack.empty()):
            current = stack.get()
            ans.append(current.val)
            
            for child in reversed(current.children):
                
                if child != None:
                    stack.put(child)
                
        
        return ans
    
    
    def preOderRecursive(self,root,ans):
        
        if root == None:
                return
        
        ans.append(root.val)
        for child in root.children:
           
            
           # print(ans)
            self.preOderRecursive(child,ans)
        
        return
        
        
