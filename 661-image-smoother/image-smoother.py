class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS , COLS = len(img) , len(img[0])
        NEW = [[0] * COLS for _ in range(ROWS)]
        for a in range(ROWS):
            for b in range(COLS):
                total, number = 0,0
                for i in range(a-1, a+2):
                    for j in range(b-1, b+2):
                        if i< 0 or i == ROWS or j<0 or j == COLS:
                            continue
                        else:
                            total += img[i][j]
                            number +=1
                NEW[a][b] = total//number
        return NEW
            

        