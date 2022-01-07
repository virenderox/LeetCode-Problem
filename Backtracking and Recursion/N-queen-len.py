class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        grid = []
        tmpAns = []
        
        for i in range(n):
            g = []
            for j in range(n):
                g.append('.')
            
            grid.append(g)
                
        self.nQueens(grid,0,n,ans,tmpAns)
        #print(tmpAns)
        answer = self.printInformat(ans,n)
        #print(grid)
        return len(answer)
    
    
    def nQueens(self,grid,current,n,ans,tmpAns):
        #tmpAns = []
        if current == n:
            ans.append(grid)
            tmpAns = deepcopy(ans)
            #print(ans is ans)
            #print("val of ans: ", tmpAns)

            return
        
        for currentCol in range(n):
            
            if self.isValid(current,currentCol,grid,n):
                
                grid[current][currentCol] = 'Q'
                self.nQueens(grid,current + 1, n ,ans,tmpAns)
                grid[current][currentCol] = '.'
        #print("val of ans: ", ans)
        #print(tmpAns)
        #return tmpAns
    
    def isValid(self,current,currentCol,grid,n):
        return self.isRowValid(current,grid,n) and self.isColValid(currentCol,grid,n) and self.isDigValid(grid,current,currentCol,n)
    
    def printInformat(self,ans,n):
        
       # print(ans)
        lst = []
        for inside in ans:
            l = []
            
            for val in inside:
                temp = ""
                
                for k in val:
                    temp += k
                    
                l.append(temp)
                
            lst.append(l)
            
        return(lst)
            
    
    def isRowValid(self,current,grid,n):
        
        for j in range(n):
            if grid[current][j] == 'Q':
                return False
            
        return True
    
    
    def isColValid(self,currentCol,grid,n):
        
        for i in range(n):
            if grid[i][currentCol] == 'Q':
                return False
            
        return True
    
    def isDigValid(self,grid,current,currentCol,n):
        
        i = current
        j = currentCol
        
        while i >= 0 and j >= 0:
            
            if grid[i][j] == 'Q':
                return False
            
            i -= 1
            j -= 1
            
            
            
            
        i = current
        j = currentCol
        
        while i >= 0 and j < n :
            
            if grid[i][j] == 'Q':
                return False
            
            i -= 1
            j += 1
            
            
            
    
            
        i = current
        j = currentCol     
        while i < n and j < n:
            
            if grid[i][j] == 'Q':
                return False
            
            i += 1
            j += 1
            
            
        
            
        i = current
        j = currentCol   
        while i < n  and j >= 0:
            
            if grid[i][j] == 'Q':
                return False
            
            i += 1
            j -= 1
            
        return True
        
        
        
