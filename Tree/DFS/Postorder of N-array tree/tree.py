class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        
        self.postOder(root,ans)
        return ans
    
    
    def postOder(self,root,ans):
        
        if root == None:
            return
        
        
        for child in root.children:
            self.postOder(child,ans)
        ans.append(root.val)
        
        return
