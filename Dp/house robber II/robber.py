class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if not nums:
            return 0
        if sum(nums) == 0:
            return 0
        return max(self.HouseRob(nums[1:],0,{}),self.HouseRob(nums[:-1],0,{})) # caller Funtion
    
    
    def HouseRob(self, nums,currentIndx, memo): # Rcursive Defination Where memo is dict for hashing
        
        if currentIndx >= len(nums): 
            return 0; # base condition
        
        currentKey = currentIndx # saving our current index to dict key
        
        if memo.get(currentKey): #if currentKey key is present then return the value of it
            return memo[currentKey] # return the value of Current Key
        
        
        rob = nums[currentIndx] + self.HouseRob(nums,currentIndx + 2,memo)# this recursive call when we will rob
        notRob = self.HouseRob(nums,currentIndx + 1,memo)# this recursive call when we cant rob and check for next possiblites
        
        
        maxMoney = max(rob, notRob)
        memo[currentIndx] = maxMoney # putting value before returning it
        
        return maxMoney
        
        
