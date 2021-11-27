# 200

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        step1 : we will traverse thru each element of the grid and if the 
        element is '1'(This confirms that at least this cell is an island)
        
        Step2 : Now we we find the neighbours of the current cell which 
        has a '1' and see whether any of the neighbours is also an 
        island which can be combined with the current one. 
        Before proceeding to find the neighbours, we change the 
        current cell's value as '0'(or any other value other than '1'), 
        so that it will not be traveresed again, while considering the 
        neighbours of any other cell.
        '''
        if not grid:
            return 0
        
        row,col = len(grid),len(grid[0])
        islands = 0
        
        
        # step2: finding '1' in the neighbours of the current cell
        def dfs(r,c):
            grid[r][c] = 0
            nbrs = [(r,c+1),(r+1,c),(r,c-1),(r-1,c)]
            for nx,ny in nbrs:
                if nx in range(row) and ny in range(col) and grid[nx][ny] == '1':
                    dfs(nx,ny)
            
            
            
        # step1: traversing the grid
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands +=1
        return islands
