class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        self.powerset(nums,0,[],powerSet)
        return powerSet
    
    
    def powerset(self,nums,current,lst,powerSet):
        
        
        if current >= len(nums):
           # print(lst)
            currentSubset = lst[:]
            powerSet.append(currentSubset) 
           # print(powerSet)
            return
            
        
        lst.append(nums[current]) 
       # print(lst)
        self.powerset(nums,current + 1,lst, powerSet)
        
        del lst[-1]
        
        self.powerset(nums,current + 1, lst, powerSet)
        return 
        #print(powerSet)
