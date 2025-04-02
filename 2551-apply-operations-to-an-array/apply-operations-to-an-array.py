class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i==len(nums)-1:
                break
            
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1]=0
        num = nums.count(0)
        nem=[i for i in nums if i!=0]
        nem.extend([0]*num)
        
                


    
        

        return nem