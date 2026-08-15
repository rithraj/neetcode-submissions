class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for end in range(1, n):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start <= 2:
                        dp[start][end] = True
                        count += 1
                    elif dp[start+1][end-1]:
                        dp[start][end] = True
                        count += 1
        
        return count 
                    
        