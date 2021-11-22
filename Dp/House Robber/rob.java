class Solution{
    public int  rob( int[] nums){
        return HouseRob(nums , 0 , new HashMap<Integer, Integer>()); // caller Funtion
    }
    
    public int  HouseRob( int[] nums,int currentIndx, HashMap<Integer, Integer> memo){ // Rcursive Defination Where memo is dict for hashing
        
        
        if(currentIndx >= nums.length)
            return 0; // base condition
        
        int currentKey = currentIndx ; //saving our current index to dict key
        
        if(memo.containsKey(currentKey))//if currentKey key is present then return the value of it
            return memo.get(currentKey); // return the value of Current Key
        
        
        int rob = nums[currentIndx] + HouseRob(nums,currentIndx + 2,memo);// this recursive call when we will rob
        int notRob = HouseRob(nums,currentIndx + 1,memo);// this recursive call when we cant rob and check for next possiblites
        
        
        int maxMoney = Math.max(rob, notRob);
        memo.put(currentIndx, maxMoney); // putting value before returning it
        
        return maxMoney;
        }
}
        
        
            
        
