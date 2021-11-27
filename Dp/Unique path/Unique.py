class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.UniquePaths(m,n,0,0,{})
    
    def UniquePaths(self,m,n,row,column,memo):
        
        if row > m-1 or column > n -1 :
            return 0
        
        if row == m-1 or column == n-1:
            return 1
        
        currentKey = (row,column)
        
        if currentKey in memo:
            return memo[currentKey]
        
        right = self.UniquePaths(m,n,row,column + 1,memo)
        down = self.UniquePaths(m,n,row+1,column ,memo)
        
        memo[currentKey] = right + down
        
        return memo[currentKey]
            
        
