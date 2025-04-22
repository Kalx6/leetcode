class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flip_value=[]
        control_index=len(arr)
        while control_index>1:
            index_of_max_value=arr.index(max(arr[0:control_index]))


            if index_of_max_value != control_index-1:
                if index_of_max_value != 0:
                    arr[:index_of_max_value+1]=list(reversed(arr[:index_of_max_value+1]))
                    flip_value.append(index_of_max_value+1)
                arr[:control_index]=list(reversed(arr[:control_index]))
                flip_value.append(control_index)
            control_index -=1
        
       

        
        
        return flip_value
        
        