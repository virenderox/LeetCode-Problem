class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefixSum = ans = 0
        #prefixSumDivide = 
        memo ={0:1} 
        
        for val in nums:
            prefixSum += val
            
            prefixSumDivide =  prefixSum % k
            
            if prefixSumDivide in memo:
                ans += memo[prefixSumDivide]
                memo[prefixSumDivide] += 1
                
            else:
                
                memo[prefixSumDivide] = 1
                
        return ans
