class Solution:
    def maximumPath(self, N, Matrix):
        ans = 0
        memo = {}
        for col in range(0,N):
            tempAns = self.MaxPath(0,col,Matrix ,N,memo)
            ans = max(ans,tempAns)
        return ans
    
    def MaxPath(self,row,column,Matrix,N,memo):
        
        if  row >=N or column < 0 or column >= N:
            return 0
            
        if row == N-1:
            return Matrix[row][column]
        
        
        currentKey = (row,column)
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        down = Matrix[row][column] + self.MaxPath(row + 1, column,Matrix,N,memo)
        dl = Matrix[row][column] + self.MaxPath(row + 1, column - 1,Matrix,N,memo)
        dr = Matrix[row][column] + self.MaxPath(row + 1, column + 1,Matrix,N,memo)
        memo[currentKey] = max(down,dl,dr)
        
        return memo[currentKey]
            
        
