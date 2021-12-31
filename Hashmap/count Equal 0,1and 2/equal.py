#User function Template for python3

class Solution:

    def getSubstringWithEqual012(self, num):
        
        ans = 0
        
        memo = {}
        
        countZeros = countOnes= countTwos = 0
        
        key = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
        
        memo[key] = 1
        
        lenS = len(num)
        for i in range(lenS):
            
            if num[i] == '0':
                countZeros += 1
                
            elif num[i] == '1':
                countOnes += 1
                
            else:
                countTwos += 1
                
            currentKey = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
            
            if currentKey in memo:
                ans += memo[currentKey]
                memo[currentKey] += 1
                
            else:
                memo[currentKey] = 1
                
        
        return ans
        

    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.getSubstringWithEqual012(Str))

# } Driver Code Ends
