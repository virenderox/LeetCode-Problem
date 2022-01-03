#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK (self,nums,  n, K) : 
        prefixSum = ans = 0
        #prefixSumDivide = 
        memo = {}
        memo[prefixSum] = -1
       # lenNums = len(nums)
        for val in range(n):
            prefixSum += nums[val]
            
            prefixSumDivide =  prefixSum % K
            
            if prefixSumDivide in memo:
                prevIndx = memo[prefixSumDivide]
                ans = max(ans, val - prevIndx )
                
            else:
                
                memo[prefixSumDivide] = val
                
        return ans
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    for _ in range(0,int(input())):
        n, K = map(int ,input().split())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        res = ob.longSubarrWthSumDivByK(arr, n, K)
        print(res)




# } Driver Code Ends
