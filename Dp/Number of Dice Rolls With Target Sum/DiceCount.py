class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.DiceCount(d,f,target,{}) % (10**9  + 7)
    
    
    def DiceCount(self,d,f,target,memo):
        
        if d == 0 and target != 0:
            return 0
        
        if d == 0 and target == 0:
            return 1
        
        currentKey = (d,target)
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        count = 0
        for face in range(1,f+1):
            count += self.DiceCount(d-1,f,target - face, memo)
            
        memo[currentKey] = count
        
        return memo[currentKey]
            
            
        
        
