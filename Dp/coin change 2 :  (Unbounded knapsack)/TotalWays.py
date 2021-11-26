class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return   self.TotalWays(coins,amount,0,{})
    
    def TotalWays(self,coins,amount,current,memo):
        
        if amount == 0:
            return 1

        if current >= len(coins) :
            return 0
        
        
        currentKey = (current , amount)
        
        consider = 0
        
        if currentKey in memo:
            return memo[currentKey]
        
        if coins[current] <= amount:
            consider =  self.TotalWays(coins,amount - coins[current], current, memo)
            
        notConsider = self.TotalWays(coins,amount, current + 1, memo)
        
        memo[currentKey] = consider + notConsider
        
    
        
        return memo[currentKey]

    
    
    
