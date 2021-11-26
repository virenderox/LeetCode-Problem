# After applying all optimizing scince got TLE cus constrain is big so we reqired grredy approch

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        return self.isPossible(nums,0,{})
    
    def isPossible(self,nums,current,memo):
        
        if current >= len(nums)-1:
            return True
        
        currentKey = current
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        currentJump = nums[current]
        ans = False
        
        for i in range(1,currentJump + 1):
            tempAns = self.isPossible(nums,current + i, memo)
            if tempAns:
                return True
            
            ans = ans or tempAns
            
        memo[currentKey] = ans
        
        return ans
        
        
        
