class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
        ans = 1
        for child in root.children:
            #print(child)
            tmp = 1 +  self.maxDepth(child)
            ans =  max(ans,tmp)
            
        return ans
            
        
        
