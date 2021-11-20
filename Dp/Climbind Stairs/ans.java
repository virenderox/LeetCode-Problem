class Solution {
    public int climbStairs(int n) {
        
        return NoOfWays(0,n, new HashMap<Integer , Integer>());
        
    }
    
    public int NoOfWays(int currentStair , int targetStair, HashMap<Integer, Integer> memo){
        
        if(currentStair == targetStair)
            return 1;
        if(currentStair > targetStair)
            return 0;
        
        int currentKey = currentStair;
        
        if(memo.containsKey(currentKey))
            return memo.get(currentKey);
        
        int oneSteps = NoOfWays(currentStair + 1, targetStair,memo);
        int secondSteps = NoOfWays(currentStair + 2, targetStair,memo);
        
        memo.put(currentKey, oneSteps + secondSteps);
        
        return oneSteps + secondSteps;
    }
}
