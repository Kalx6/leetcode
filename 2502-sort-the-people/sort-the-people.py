class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        import copy

        ret = [0]*len(names)

        copy_height = copy.deepcopy(heights)

        copy_height.sort(reverse=True)

        for i in range(len(names)):
            ret[i] = names[heights.index(copy_height[i])]
        

        return ret


      
        

        
