from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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
            
                if currentNode.left != None:
                    q.put(currentNode.left)
            
                if currentNode.right != None:
                    q.put(currentNode.right)
                
                currentLevel -= 1
            ans.append(level)
                
        return ans
    
    
