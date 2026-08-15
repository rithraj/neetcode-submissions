class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        
        def dfs(i, j):
            stack = []
            if grid[i][j] == "1" and (i,j) not in visited:
                stack.append((i,j))
                visited.add((i,j))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while stack:
                y,x = stack.pop()
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if ny >=0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]) and grid[ny][nx] == "1" and (ny, nx) not in visited:
                        stack.append((ny, nx))
                        visited.add((ny, nx))

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count += 1
        
        return count


        