# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        lstRoot1 = []
        lstRoot2 = []
    
        
        self.inOrder(root1,lstRoot1)
        self.inOrder(root2,lstRoot2)
        
        comlst = []
        lenRoot1 = len(lstRoot1)
        lenRoot2 = len(lstRoot2)
        i = 0
        j = 0
        while i < lenRoot1 and j < lenRoot2:
            #print(i,j)
            if lstRoot1[i] > lstRoot2[j]:
                comlst.append(lstRoot2[j])
                j += 1
            else:
                comlst.append(lstRoot1[i])
                i += 1
        if i == lenRoot1:
            comlst += lstRoot2[j:]
        if j == lenRoot2:
            comlst += lstRoot1[i:]
        return comlst
    
    def inOrder(self,root,lst):
        
        if root == None:
            return
        
        self.inOrder(root.left,lst)
        lst.append(root.val)
        self.inOrder(root.right,lst)
        
        
        return
        
