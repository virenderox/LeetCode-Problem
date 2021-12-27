
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        memo = {}
        lst = []
        uniqueElements = 0
        for i in range(K-1):
            
            if A[i] in memo:
                memo[A[i]] += 1
            else:
                memo[A[i]] = 1
                uniqueElements += 1
                
        init = 0
        while(N >= K):
            
            release = A[init]
            accquire = A[K-1]
           # print(release, accquire)
            if accquire in memo:
                memo[accquire] += 1
            else:
                memo[accquire] = 1
                uniqueElements += 1
            
            lst.append(uniqueElements)
            
            memo[release] -= 1
            if memo[release] == 0:
                #print(K)
                del memo[release]
                uniqueElements -= 1
            K = K + 1
            init += 1
            
                
            
                
        #print(memo, uniqueElements)
        
        return lst

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends
