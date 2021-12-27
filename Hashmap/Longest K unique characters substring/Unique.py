#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        ans = -1 
        left = 0
        memo = {}
        lenS = len(s)
        for right in range(lenS):
            currentChar = s[right]
            
            if currentChar in memo:
                memo[currentChar] += 1
                
            else:
                memo[currentChar] = 1
                
            while left <= right and len(memo) > k:
                disChar = s[left]
                memo[disChar] -= 1
                
                left += 1
                
                if memo[disChar] == 0:
                    del memo[disChar]
                    
            if len(memo) == k:
                ans = max(ans, right - left + 1)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends
