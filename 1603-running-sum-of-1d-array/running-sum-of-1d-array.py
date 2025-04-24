class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret=[]
        a=0
        for i in nums:
            a+=i
            ret.append(a)




        return ret
        