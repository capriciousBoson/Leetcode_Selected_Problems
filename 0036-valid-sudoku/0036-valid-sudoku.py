class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for  _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
            
                n = board[i][j]
                # check row
                if n in rows[i]:
                    return False
                else:
                    rows[i].add(n)
                #  check col
                if n in cols[j]:
                    return False
                else:
                    cols[j].add(n)
                # check grid
                g = (i//3)+((j//3)*3)
                if n in grids[g]:
                    return False
                else:
                    grids[g].add(n)
        return True