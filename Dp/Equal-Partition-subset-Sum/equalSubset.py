class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2 :
            return False
        return self.EqualPart(nums,0,numSum//2,{})
        
    def EqualPart(self,nums,current,target,memo):
        
        if target == 0:
            return True
        
        if current >= len(nums):
            return False
        
        currentKey = (current, target)
        
        if currentKey in memo:
            return memo[currentKey]
        
        consider = False
        
        if nums[current] <= target:
            consider = self.EqualPart(nums,current + 1, target - (nums[current]), memo)
            
        notConsider = self.EqualPart(nums,current + 1, target, memo)
        
        memo[currentKey] = consider or notConsider
        
        return memo[currentKey]
        
