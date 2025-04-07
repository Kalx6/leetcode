class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res= []
        res_1=[]
        for x in arr2:
            arr1_no= arr1.count(x)
            res.extend([x]*arr1_no)
        for y in arr1:
            if y  not in arr2:
                res_1.append(y)
        res_1.sort()
        res.extend(res_1)
        return res
        
        


        