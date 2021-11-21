class Solution:
    def fib(self, n: int) -> int:
        return self.nthFib(n,{})
    
    def nthFib(self,n,memo):
        
        if n == 0:
            return 0;
        if n == 1:
            return 1;
        
        currentKey = n
        
        if memo.get(currentKey):
            return memo[currentKey]
        
        nthFib = self.nthFib(n-1,memo) + self.nthFib(n-2,memo)
        
        memo[n] = nthFib
        
        return nthFib
        
