# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
    
        hashSet = set()
        self.RightSideView(root,1,hashSet,ans)
        return ans
    
    def RightSideView(self,root, level,hashSet , ans):

        if root == None:
            return;

        if not (level in hashSet):
            hashSet.add(level)
            ans.append(root.val)

        self.RightSideView(root.right,level + 1,hashSet,ans)
        self.RightSideView(root.left,level + 1,hashSet,ans)

        return

        
