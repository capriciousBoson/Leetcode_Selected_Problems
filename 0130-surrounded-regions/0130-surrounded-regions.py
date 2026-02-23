class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows,cols = len(board), len(board[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        q = collections.deque()

        for r in range(rows):
            if board[r][0] == 'O':
                q.append((r,0))
            if board[r][cols-1] == 'O':
                q.append((r, cols-1))
        
        for c in range(cols):
            if board[0][c] == 'O':
                q.append((0,c))
            if board[rows-1][c] == 'O':
                q.append((rows-1, c))
        
        while q:
            i,j = q.popleft()
            board[i][j] = '#'
            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<rows and 0<=y<cols and board[x][y] == 'O':
                    q.append((x,y))
        
        for i_ in range(rows):
            for j_ in range(cols):
                if board[i_][j_] == 'O':
                    board[i_][j_] = 'X'

                elif board[i_][j_] == '#':
                    board[i_][j_] = 'O'


        