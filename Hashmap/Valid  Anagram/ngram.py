class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        memo = {}
        
        for valS in s:
            
            if valS in memo:
                memo[valS] += 1
            else:
                memo[valS] = 1
                
        for valT in t:
            
            if valT not in memo:
                return False
            
            else:
                memo[valT] -= 1
                
                
            if memo[valT] == 0:
                del memo[valT]
                
        
        return len(memo) == 0
