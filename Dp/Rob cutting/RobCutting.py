#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        return self.cut(price,n,0,{})
        
    def cut(self,price,n,current, memo):
        
        if n == 0:
            return 0
        if current >= len(price):
            return 0
            
        currentKey = (current, n)
        
        if memo.get(currentKey):
            return memo[currentKey]
        
        consider = 0   
        
        if current + 1 <= n:
            
            consider = price[current] + self.cut(price , n - (current + 1) , current, memo) 
            
        notConsider = self.cut(price,n,current + 1, memo)
        
        maxProfit = max(consider,notConsider)
        
        memo[current] = maxProfit
        
        return maxProfit
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
