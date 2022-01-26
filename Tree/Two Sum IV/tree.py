class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        its a brute force approch not optimal way as Tc( O(n**2))
        lst = []
        self.convert(root,lst)
        
        ln = len(lst)
        for i in range(1,ln+1):
            for j in range(i,ln):
                #print(lst[i-1],lst[j])
                if lst[i-1] + lst[j] == k:
                    return True
        return False
        
        can we do better in O(n)
        
       
        if root == None:
            return False
        
        return self.findComplement(root,set(),k)
        
    
     """
        ans = []
        
        self.convert(root,ans)
        left = 0
        right = len(ans) - 1
        
        while(left < right):
            
            if ans[left] + ans[right] == k:
                return True
            elif ans[left] + ans[right] > k:
                right -= 1
            else:
                left += 1
        return False
        
    def findComplement(self,root,node,k):
        
        if root == None:
            return False
        
        complement = k - root.val
        
        if complement in node:
            return True
        
        node.add(root.val)
        
        return self.findComplement(root.left,node,k) or self.findComplement(root.right,node,k)
        
        
    def convert(self,root,ans):
        
        if root == None:
            return 
        
        
        self.convert(root.left,ans)
        ans.append(root.val)
        self.convert(root.right,ans)
        
        return
        
