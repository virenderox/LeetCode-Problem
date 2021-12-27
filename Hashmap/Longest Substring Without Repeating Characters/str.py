class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        memo = {} # key char of s and value will be the index of that character
        
        ans = 0
        left = 0
        lenS = len(s)
        
        for currentIndex in range(lenS):
            char = s[currentIndex]
            
            if char not in memo:
                memo[char] = currentIndex
                
            else: 
                tmpLeft  =  (memo[char] + 1)
                if tmpLeft > left:
                    left = tmpLeft
                memo[char] = currentIndex
                
           # print("current" , currentIndex, "left" , left)
            tmpAns = currentIndex - left + 1
            #print(tmpAns)
            
            if tmpAns > ans:
                ans = tmpAns
                
        return ans
            
        
