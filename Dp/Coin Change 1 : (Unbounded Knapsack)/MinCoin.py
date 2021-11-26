class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        count =  self.MinCoin(coins,amount,0,{})
        if count == 100000:
            return -1
        else: 
            return count
    
    
    def MinCoin(self,coins,amount,current,memo):
        
        if amount == 0:
            return 0

        if current >= len(coins) :
            return 100000
        
        
        currentKey = (current , amount)
        
        consider = 100000
        if currentKey in memo:
            return memo[currentKey]
        
        if coins[current] <= amount:
            consider = 1 + self.MinCoin(coins,amount - coins[current], current, memo)
            
        notConsider = self.MinCoin(coins,amount, current + 1, memo)
        
        memo[currentKey] = min(consider,notConsider)
        
    
        
        return memo[currentKey]

    
    
    
