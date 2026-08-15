class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        init = 0
        max_len = 1
        for i in range(n):
           dp[i][i] = True

        for end in range(1, n):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start <= 2:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start + 1][end - 1]

                if dp[start][end] and end - start + 1 > max_len:
                    init = start
                    max_len = end - start + 1
                
        return s[init: init+max_len]
        