class Solution:
    def islandsAndTreasure(self, grid) -> None:
        
        def move(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c]==-1 or (r,c) in visit): return
            visit.add((r,c))
            q.append([r,c])




        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        
        # getting all the gates/chests
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c] = distance
                
                move(r+1,c)
                move(r-1,c)
                move(r,c+1)
                move(r,c-1)
            distance += 1
                
