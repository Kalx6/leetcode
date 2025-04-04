class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        res = [[] for i in range(ROWS+COLS)]
        final_list=[]
        for r in range(ROWS):
            for c in range(COLS):
                res[r+c].append(mat[r][c])
        for i in range(len(res)):
            if i%2==0:
                res[i].reverse()
         
        return sum(res,[])

        