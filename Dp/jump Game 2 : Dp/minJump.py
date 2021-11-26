# preffred to take greedy approch

class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.minJump(nums,0,{})
    
    def minJump(self,nums,current,memo):
        
        if current >= len(nums)-1:
            return 0
        
        currentKey = current
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        currentJump = nums[current]
        ans = 10000
        
        for i in range(1,currentJump + 1):
            tempAns = 1 + self.minJump(nums,current + i, memo)
            ans = min(ans, tempAns)
            
        memo[currentKey] = ans
        
        return ans
        
