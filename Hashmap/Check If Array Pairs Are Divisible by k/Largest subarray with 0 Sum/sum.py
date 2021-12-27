#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        prefixSum = 0
        memo = {prefixSum : -1}
        maxLen = 0
        for i in range(n):
            val = arr[i]
            prefixSum += val
            if prefixSum in memo:
                currentLen = i - memo[prefixSum]
                if currentLen > maxLen:
                    maxLen = currentLen
                
            else:
                memo[prefixSum] = i
        return maxLen

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
