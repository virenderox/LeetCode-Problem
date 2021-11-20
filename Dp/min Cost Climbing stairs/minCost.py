class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        return min(self.MinCostStair(0, len_cost,cost,{}),self.MinCostStair(1, len_cost,cost,{}))
    
    def MinCostStair(self,current,target,cost,memo):
        
        if current == target:
            return 0
        
        if current > target:
            return math.inf
        
        currentKey = current
        
        if memo.get(currentKey):
            return memo[currentKey]
        
        oneJump = cost[current] + self.MinCostStair(current+1,target,cost,memo)
        secondJump = cost[current] + self.MinCostStair(current+2,target,cost,memo)
        
        memo[current] = min(oneJump, secondJump)
        
        return min(oneJump, secondJump)
