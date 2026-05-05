class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []


        def dfs(k,row_idx,board,cols,l_diag, r_diag):

            if k==n:
                res.append(["".join(row) for row in board])
                return 

            for c in range(n):
                if c not in cols and (row_idx - c) not in l_diag and (row_idx + c) not in r_diag:

                    #place the queen
                    board[row_idx][c]="Q"
                    #mark attacked positions in the below rows
                    cols.add(c)
                    l_diag.add(row_idx-c)
                    r_diag.add(row_idx+c)

                    # recursive function call
                    dfs(k+1,row_idx+1,board,cols, l_diag, r_diag)

                    #unmark attacked rows
                    board[row_idx][c]="."
                    cols.remove(c)
                    l_diag.remove(row_idx-c)
                    r_diag.remove(row_idx+c)

            return

        x = [["." for i in range(n)] for i in range(n)]
        dfs(0,0,x, set(),set(),set())
        return res




