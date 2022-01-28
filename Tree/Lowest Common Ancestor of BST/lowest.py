class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current = root
        
        while current != None:
            
            if current.val > p.val and current.val > q.val:
                current = current.left
                
            elif current.val < p.val and current.val < q.val:
                current = current.right
                
            else:
                return current
            
        return None
                
