class Solution:
    def minFallingPathSum(self, Matrix: List[List[int]]) -> int:
        ans = 10000
        memo = {}
        N = len(Matrix)
        for col in range(0,N):
            tempAns = self.MinPath(0,col,Matrix ,N,memo)
            ans = min(ans,tempAns)
           # print(ans,tempAns)
        return ans
    
    def MinPath(self,row,column,Matrix,N,memo):
        
        if  row >=N or column < 0 or column >= N:
            return 10000
            
        if row == N-1:
            return Matrix[row][column]
        
        
        currentKey = (row,column)
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        down = Matrix[row][column] + self.MinPath(row + 1, column,Matrix,N,memo)
        dl = Matrix[row][column] + self.MinPath(row + 1, column - 1,Matrix,N,memo)
        dr = Matrix[row][column] + self.MinPath(row + 1, column + 1,Matrix,N,memo)
        memo[currentKey] = min(down ,dl, dr)
        
        return memo[currentKey]
            
        
