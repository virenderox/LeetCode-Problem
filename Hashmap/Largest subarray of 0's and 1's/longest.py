#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        prefixSum = 0
        memo = {prefixSum : -1}
        maxLen = 0
        for i in range(n):
            val = arr[i]
            if val == 0:
                prefixSum += -1
            else:
                prefixSum += 1
            if prefixSum in memo:
                currentLen = i - memo[prefixSum]
                if currentLen > maxLen:
                    maxLen = currentLen
                
            else:
                memo[prefixSum] = i
        return maxLen

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends
