class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        ans = []
        
        self.preOder(root,ans)
        return ans
    
    
    def preOder(self,root,ans):
        
        if root == None:
                return
        
        ans.append(root.val)
        for child in root.children:
           
            
           # print(ans)
            self.preOder(child,ans)
        
        return
        
