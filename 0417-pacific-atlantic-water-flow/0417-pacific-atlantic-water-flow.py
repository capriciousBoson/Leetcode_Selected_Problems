class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        pac = set()
        atl = set()
        
        q  = collections.deque()

        for j in range(cols):
            q.append((0,j))
        
        for i in range(rows):
            q.append((i,0))
        
        while q:
            r,c = q.popleft()
            pac.add((r,c))

            for dx, dy in dirs:
                x,y = r+dx, c+dy
                if 0<=x<rows and 0<=y<cols and heights[x][y] >= heights[r][c]:
                    if (x,y) not in pac:
                        q.append((x,y))

        q = collections.deque()
        for j in range(cols):
            q.append((rows-1,j))
        
        for i in range(rows):
            q.append((i,cols-1))

        while q:
            r,c = q.popleft()
            atl.add((r,c))

            for dx, dy in dirs:
                x,y = r+dx, c+dy
                if 0<=x<rows and 0<=y<cols and heights[x][y] >= heights[r][c]:
                    if (x,y) not in atl:
                        q.append((x,y))
        # print(f"pac : {pac} \n atl : {atl}")
        return list(pac.intersection(atl))
        



        