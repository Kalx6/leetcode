class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        indx = 0
        freinds = [i+1 for i in range(n)] 
        while len(freinds) > 1:
            indx = (indx + k - 1) % len(freinds)
            freinds.pop(indx)

        return freinds[0]
                
           
           
            



        