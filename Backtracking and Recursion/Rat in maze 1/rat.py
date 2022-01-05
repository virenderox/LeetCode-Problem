#User function Template for python3

class Solution:
    def findPath(self, grid, n):
        ans = []
        self.generateAllPath(grid,0,0,n,"",ans)
        #ans.sort()
        return ans
        
    def generateAllPath(self,grid,row,column,n,current,ans):
        
        if row < 0 or row >= n or column < 0 or column >= n or grid[row][column] == 0:
            return
        
        if row == n-1 and column == n-1:
            ans.append(current)
            return
        
        grid[row][column] = 0
        
        #down - move 
        self.generateAllPath(grid,row+1,column,n,current + "D",ans)
        
        #left - move 
        self.generateAllPath(grid,row,column- 1,n,current + "L",ans)
        
         #right - move 
        self.generateAllPath(grid,row,column+1,n,current + "R",ans)
        
        #up - move 
        self.generateAllPath(grid,row-1,column,n,current + "U",ans)
        
       
        
        
       
        
        grid[row][column] = 1
        return




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
