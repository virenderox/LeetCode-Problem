class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        ans = distinctCount = release = 0
    
        memo = {}
        
        lenS = len(s)
        count = (lenS * (lenS + 1)) // 2
        for val in range(lenS):
            
            accquire = s[val]
            if accquire in memo:
                memo[accquire] += 1
                
            else:
                distinctCount += 1
                memo[accquire] = 1
                
                
            while release <= val and distinctCount > k-1:
                
                disChar = s[release]
                memo[disChar] -= 1
                
                release += 1
                
                if memo[disChar] == 0:
                    del memo[disChar]
                    distinctCount -= 1
                    
                
            ans += (val - release + 1)
            
        return count - ans
