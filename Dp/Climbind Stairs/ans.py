class Solution:
    def climbStairs(self, n: int) -> int:
        return self.noOfWays(0,n, {})
    
    def noOfWays(self,currentStair,targetStair, memo):
        count = 0
        if currentStair == targetStair:
            return 1
            
        if currentStair > targetStair:
            return 0;
        currentKey = currentStair
        
        if memo.get(currentKey):
            return memo[currentKey]
        
        oneStep = self.noOfWays(currentStair + 1,targetStair, memo )
        twoStep = self.noOfWays(currentStair + 2,targetStair, memo )
        
        memo[currentStair ] = oneStep + twoStep
        
        return oneStep + twoStep
        
        
