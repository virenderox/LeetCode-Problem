class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.UniquePaths(obstacleGrid,m,n,0,0,{})
    
    def UniquePaths(self,obstacleGrid,m,n,row,column,memo):
        
        if row > m-1 or column > n -1 or obstacleGrid[row][column] == 1:
            return 0
        
        if row == m-1 and column == n-1:
            return 1
        
        currentKey = (row,column)
        
        if currentKey in memo:
            return memo[currentKey]
        
        right = self.UniquePaths(obstacleGrid,m,n,row,column + 1,memo)
        down = self.UniquePaths(obstacleGrid,m,n,row+1,column ,memo)
        
        memo[currentKey] = right + down
        
        return memo[currentKey]
            
        
