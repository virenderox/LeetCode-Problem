# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        ans = []
        memo = {}
        
        self.populateMap(root,None,memo)
        unique = set()
        self.printKDistance(target,k,memo,ans,unique)
        return ans
        
    def populateMap(self,current,currentParent,memo):
        
        if current == None:
            return
        memo[current] = currentParent
        self.populateMap(current.left,current,memo)
        self.populateMap(current.right,current,memo)
        return
    
    def printKDistance(self,target,k,memo,ans,unique):
        
        if target == None or target in unique :
            return
        
        unique.add(target)
        if k == 0:
            ans.append(target.val)
            return
        self.printKDistance(target.left,k-1,memo,ans,unique)
        self.printKDistance(target.right,k-1,memo,ans,unique)
        self.printKDistance(memo[target],k-1,memo,ans,unique)
        
