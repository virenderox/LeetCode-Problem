class Solution:
    def numSquares(self, n: int) -> int:
        
        lst = self.numSquares(n)
        return self.MinSquare(lst,n,0,{})
    

    def numSquares(self, n):
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3
    def MinSquare(self,lst,amount,current,memo):
        
        if amount == 0:
            return 0
        
        if current >= len(lst):
            return 10000
        
        currentKey = (current, amount)
        
        if memo.get(currentKey):
            return memo[currentKey]
        
        consider = 10000
        
        if lst[current] <= amount:
            consider = 1 + self.MinSquare(lst,amount - (lst[current]), current, memo)
            
        notConsider = self.MinSquare(lst,amount, current + 1, memo)
        
        memo[currentKey] = min(consider, notConsider)
        
        return memo[currentKey]
