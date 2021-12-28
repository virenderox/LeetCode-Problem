#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        memo = {}
        prefixSum = ans = 0
        memo[prefixSum] = 1
        
        for val in arr:
            
            if val == 0:
                prefixSum += -1
            else:
                prefixSum += 1
            
            if prefixSum in memo:
                ans += memo[prefixSum]
                memo[prefixSum] += 1
                
            else:
                memo[prefixSum] = 1
                
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
