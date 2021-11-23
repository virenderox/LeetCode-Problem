#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        return self.Kanp(W,wt,val,n,{},0)
        
    def Kanp(self,W,wt,val,n,memo,current):
        
        if current >= n:
            return 0;
            
        currentKey = (current, W)
        
        if (currentKey) in memo:
            return memo[currentKey]
            
        taken = 0  
        if((wt[current]) <= W):
            taken = val[current] + self.Kanp((W-wt[current]), wt, val,n, memo, current + 1 )
        
        notTaken = self.Kanp(W,wt,val,n,memo, current + 1) 
        
        maxProfit = max(taken, notTaken)
        
        memo[current] = maxProfit
        
        return maxProfit
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
