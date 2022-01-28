class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.arrayToBst(nums,0,len(nums) -1)
    
    def arrayToBst(self,nums,start,end):
        
        if start > end:
            return None
        
        mid = (start + end) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.arrayToBst(nums,start,mid-1)
        root.right = self.arrayToBst(nums,mid+1,end)
        
        return root
