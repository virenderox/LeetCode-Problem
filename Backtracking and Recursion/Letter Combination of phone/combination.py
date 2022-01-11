class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        memo = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        
        ans = []
        
        lenDigit = len(digits)
        
        if lenDigit == 0:
            return ans
        
        self.Combination(digits,0,lenDigit,memo,ans,"")
        return ans
    
    def Combination(self,digits,index,n,memo,ans,current):
        
        
        if index == n:
            ans.append(current)
            return
        
        mapping = memo[digits[index]]
        #lenMapping = len(mapping)
        
        for char in mapping:
            self.Combination(digits,index + 1,n,memo,ans,current + char)
            
        
