class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)

        dirs = ((0,1), (1,0), (-1,0), (0,-1))

        def find(idx, i, j):
            
            
            if board[i][j] != word[idx]:
                return False

            if idx==n-1:
                return True

            board[i][j] = '#'
            

            for dx, dy in dirs:
                x,y = dx+i, dy+j

                if 0<=x<rows and 0<=y<cols:
                    # print(f"\n\nlooking for : {word[idx+1]}  at {x,y} in -- ")
                    # for row_ in board: print(row_)
                    

                    # board[x][y] = '#'
                    found = find(idx+1, x,y)

                    # board[x][y] = word[idx]

                    if found: return True
            board[i][j] = word[idx]
            return False

        for r in range(rows):
            for c in range(cols):
                print(f"\nstarting search from : {r,c}---------------------")
                found = find(0, r,c)
                if found: return True
        return False

            

            
        