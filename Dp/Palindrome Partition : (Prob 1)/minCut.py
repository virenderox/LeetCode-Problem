class Solution:
    def minCut(self, s: str) -> int:
        return self.MinimumCut(s,0,len(s) - 1,{})
    
    def isPalindrome(self,s,start,end):
        
        while start <= end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
            
        return True
    
    
    def MinimumCut(self,s,start,end,memo):
        
        if self.isPalindrome(s,start,end) or start > end:
            return 0
        
        currentKey = start
        
        if currentKey in memo:
            return memo[currentKey]
        
        ans = 1000
        for currentCut in range(start,end):
            
            if self.isPalindrome(s,start,currentCut):
                tmpAns = 1 + self.MinimumCut(s,currentCut + 1,end,memo)
                ans = min(ans,tmpAns)
                
        memo[currentKey] = ans
        
        return memo[currentKey]
        
        
    
   
