class Solution:
    def combinationSum(self, coins: List[int],amount: int) -> List[List[int]]:

        output = []
        self.MinCoin(coins,amount,0,[], output)
        return output
    
    def MinCoin(self,coins,amount,current,currentSet, output):
        
        if amount == 0:
            output.append(currentSet[:])
            return

        if current >= len(coins) :
            return
        
        currentVal = coins[current]
        if amount >= currentVal:
            currentSet.append(currentVal)
            self.MinCoin(coins,amount - currentVal, current,currentSet,output)
            currentSet.pop()
            
        self.MinCoin(coins,amount, current + 1,currentSet,output)
        
        return

    
    
