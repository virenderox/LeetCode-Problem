class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.MinPathSum(grid,m,n,0,0,{})
    
    def MinPathSum(self,grid,m,n,row,column,memo):
        
        if row > m-1 or column > n -1 :
            return 10000
        
        if row == m-1 and column == n-1:
            return grid[row][column]
        
        currentKey = (row,column)
        
        if currentKey in memo:
            return memo[currentKey]
        
        right = grid[row][column] + self.MinPathSum(grid,m,n,row,column + 1,memo)
        down = grid[row][column] + self.MinPathSum(grid,m,n,row+1,column ,memo)
        
        memo[currentKey] = min(right , down)
        
        return memo[currentKey]
            
        
