class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c , i):
            if i == len(word):
                return True
            # Tests if out of bounds, visited, or word[i] != board[r][c] since then not valid char
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in path or word[i] != board[r][c]):
                return False
            
            # Appending to the path
            path.add((r, c))
            
            # Result value needs to be a boolean
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            # Remove from the path (popping off for backtracking)
            path.remove((r, c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False