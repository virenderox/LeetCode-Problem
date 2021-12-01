class Solution:
    def numTrees(self, n: int) -> int:
        return self.nthCatalan(n,{})
        
    def nthCatalan(self,n,memo):
        
        if n == 0 or n == 1:
            return 1
         
        currentKey = n
        
        if currentKey in memo:
            return memo[currentKey]
            
        ways = 0
        for i in range(n):
            ways += self.nthCatalan(i,memo) * self.nthCatalan(n - i - 1,memo)
        
        memo[currentKey] = ways
        
        return memo[currentKey]
        
