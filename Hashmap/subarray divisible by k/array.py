Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@virenderox 
virenderox
/
LeetCode-Problem
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
LeetCode-Problem/Hashmap/Check If Array Pairs Are Divisible by k/arrat.py /
@virenderox
virenderox Create arrat.py
Latest commit 9a751d4 3 days ago
 History
 1 contributor
47 lines (31 sloc)  1.16 KB
   
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        memo = {}
        
        for val in arr:
            
            if val < 0 :
                rem = ((val % k) + k) % k
                
                if rem in memo:
                    memo[rem] += 1
                    
                else:
                    
                    memo[rem] = 1
            
            else:
                
                rem = val % k
                
                if rem in memo:
                    memo[rem] += 1
                    
                else:
                    memo[rem] = 1
                    
        #print(memo)
            
        for key in memo:
            
            if key == 0:
                if memo[key] % 2 != 0:
                    return False
            else:
                keyVal = memo[key]
                if memo.get(k - key):
                    keyComp = memo[k - key]
                else:
                    return False
                #print(key, keyVal)
                if keyVal != keyComp:
                    return False
            
        return True
                    
        
