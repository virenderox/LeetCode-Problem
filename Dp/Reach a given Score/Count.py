#User function Template for python3

def count(target):
    
    nums = [3,5,10]
    return DisntComb(0,nums,target,{})
    
def DisntComb(current , nums, target, memo):

    if target == 0:
        return 1
    if current >= len(nums):
        return 0
        
    currentKey = (current,target)
    
    if memo.get(currentKey):
        return memo[currentKey]
        
    consider = 0
    
    if nums[current] <= target:
        consider = DisntComb(current , nums, target - nums[current], memo)
    
    notConsider = DisntComb(current + 1 , nums, target, memo)
    
    memo[currentKey] = consider + notConsider
    
    return memo[currentKey]
        
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends
