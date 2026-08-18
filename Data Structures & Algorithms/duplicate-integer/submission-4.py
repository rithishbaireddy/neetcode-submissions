class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                return True

            hashmap[i] = 1

        return False
        
        
        
        #for i in  range(len(nums)):
        ##       if(nums[i]==nums[j]):
                    #return True
                
        #return False   
        