class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        area = 0
        memo = {}
        for row in range(m):
            for column in range(n):
                
                if matrix[row][column] == '1':
                    
                    side = self.MaxLength(matrix,row,column,m,n,memo)
                    area = max(area, side * side)
        return area
    
    
    def MaxLength(self,matrix,row,column,m,n,memo):
        if  row < 0 or  row >=m or column < 0 or column >= n or matrix[row][column] == "0":
            return 0
            
        
        currentKey = (row,column)
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        down = 1 + self.MaxLength(matrix,row + 1, column,m,n,memo)
        lft= 1 + self.MaxLength(matrix, row , column + 1,m,n,memo)
        dr = 1 + self.MaxLength(matrix, row + 1, column + 1,m,n,memo)
        memo[currentKey] = min(down ,lft, dr)
        
        return memo[currentKey]
                    
