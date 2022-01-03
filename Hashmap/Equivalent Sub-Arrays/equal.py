#User function Template for python3

class Solution:
    def countDistinctSubarray(self,s, n): 
        
        k = 0
        memo = {}
        
        for i in range(n):
            currentVal = s[i]
            if currentVal in memo:
                memo[currentVal] += 1
            else:
                k += 1
                memo[currentVal] = 1
        
        return self.AtmostKUniqueChar( s,k) - self.AtmostKUniqueChar( s,k -1 )
        
    def AtmostKUniqueChar(self, s,k):
    
        ans = distinctCount = release = 0
        
        memo = {}
        
        lenS = len(s)
        for val in range(lenS):
            
            accquire = s[val]
            if accquire in memo:
                memo[accquire] += 1
                
            else:
                distinctCount += 1
                memo[accquire] = 1
                
                
            while release <= val and distinctCount > k:
                
                disChar = s[release]
                memo[disChar] -= 1
                
                release += 1
                
                if memo[disChar] == 0:
                    del memo[disChar]
                    distinctCount -= 1
                    
                
            ans += (val - release + 1)
            
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.countDistinctSubarray(a,n))




# } Driver Code Ends
