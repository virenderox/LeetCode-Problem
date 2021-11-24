class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.TotalWays(nums,0,target,{})
    
    def TotalWays(self,nums,current,target,memo):
        
        if current >= len(nums) and target != 0:
            return 0;
        
        if current >= len(nums) and target == 0:
            return 1;
        
        currentKey = (current,target)
        
        if currentKey in memo:
            return memo[currentKey]
        
        positive = self.TotalWays(nums,current + 1, target - nums[current], memo)
        
        negative = self.TotalWays(nums,current + 1, target + nums[current], memo)
        
        
        memo[currentKey] = positive + negative
        
        return memo[currentKey]
        
