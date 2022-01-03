#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        countAtMostK = self.AtmostKUniqueChar(s,k)
        countAtMostK_1 = self.AtmostKUniqueChar(s,k-1)
        
        return countAtMostK - countAtMostK_1
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

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends
