"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = Queue()
        ans = []
        
        if root == None:
            return ans
        
        q.put(root)
        
        while not q.empty():
            
            currentLevel = q.qsize()
            level = []
            while(currentLevel > 0):
                
                currentNode = q.get()
    
                level.append(currentNode.val)
                for child in currentNode.children:
            
                    q.put(child)
                
                currentLevel -= 1
            ans.append(level)
                
        return ans
    
    
        
