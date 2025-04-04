class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict={}
        res=[]
        for i in range(len(names)):
            my_dict[heights[i]]=names[i]
        
        heights.sort(reverse=True)

        for i in heights:
            
            res.append(my_dict[i])
        

        return res

      
        

        