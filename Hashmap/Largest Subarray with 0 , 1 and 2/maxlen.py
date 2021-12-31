def largestSubarry(num,N):
    ans = 0
    
    memo = {}
    
    countZeros = countOnes= countTwos = 0
    
    key = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
    
    memo[key] = -1
    
    
    for i in range(N):
        
        if num[i] == 0:
            countZeros += 1
            
        elif num[i] == 1:
            countOnes += 1
            
        else:
            countTwos += 1
            
        currentKey = str(countOnes - countZeros) + '#' + str(countTwos - countOnes)
        
        if currentKey in memo:
            prev = memo[currentKey]
            leng = i - prev
            ans = max(ans,leng)
        else:
            memo[currentKey] = i
            
    
    return ans
    
n = int(input())
lst = list(map(int, input().split(" ")))
ans = largestSubarry(lst,n)
print(ans)
    
    
    
