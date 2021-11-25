class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
         return self.BestTime(prices,0,True,k,{}) # this is our calling function
    
    def BestTime(self,prices,currentDay , canBuy, transCount, memo):
        '''
        input parameters
            prices : this is arry which contain prices for transaction
            currentDay : this is the starting index of our method call
            canBuy : this is boolean variable which indicates   
                    
                    true : we can buy the at that particular currentDay
                    false : we buy that product and we cannot buy further
                    
            transCount : this indicates the total transaction we have to make
            memo : this is hashmap for storing the repeated method calling
            
        output : maxProfit after the transcation made

        '''
        
        # base condition
        if currentDay >= len(prices) or transCount <= 0:
            return 0;
        
        # making of key for hashmap
        currentKey = (currentDay,canBuy,transCount) 
        
        # if method call already present return their only
        if currentKey in memo:
            return memo[currentKey]
        
        # our recursive call -> if can sit ideal or buy the stock on that particular day
        if canBuy:
            ideal = self.BestTime(prices,currentDay + 1,canBuy, transCount, memo) # we sit ideal at that day
            buy = -prices[currentDay] + self.BestTime(prices,currentDay + 1,False, transCount, memo) # we buy the stock at that day
            memo[currentKey] = max(ideal,buy)
            return memo[currentKey]
        else:
            ideal = self.BestTime(prices,currentDay + 1,canBuy, transCount, memo) # we sit ideal at that day
            sell = prices[currentDay] + self.BestTime(prices,currentDay + 1,True, transCount - 1, memo) # we sell the stock at that day
            memo[currentKey] = max(ideal,sell)
            return memo[currentKey]
            
        
