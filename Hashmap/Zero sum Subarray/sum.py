#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        memo = {}
        prefixSum = ans = 0
        memo[prefixSum] = 1
        
        for val in arr:
            
            prefixSum += val
            
            if prefixSum in memo:
                ans += memo[prefixSum]
                memo[prefixSum] += 1
                
            else:
                memo[prefixSum] = 1
                
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends
