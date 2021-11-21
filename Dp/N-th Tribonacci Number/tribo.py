class Solution:
    def tribonacci(self, n: int) -> int:
        return self.nthtribo(n,{})
    
    def nthtribo(self,n,memo):
        
        if n == 0:
            return 0;
        if n == 1 or n == 2:
            return 1;
        
        currentKey = n
        
        if memo.get(currentKey):
            return memo[currentKey]
        
        nthFib = self.nthtribo(n-1,memo) + self.nthtribo(n -2,memo) + self.nthtribo(n - 3,memo)
        
        memo[n] = nthFib
        
        return nthFib
