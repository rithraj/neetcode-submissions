class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        
        # memo = {}

        # def dfs(target):
        #     if target == 0:
        #         return 0
        #     if target in memo:
        #         return memo[target]
        
        #     res = float('inf')
        #     for coin in coins:
        #         if target - coin >= 0:
        #             res = min(res, 1 + dfs(target - coin))
            
        #     memo[target] = res
        #     return res

        # minCoins = dfs(amount)
        # if minCoins >= float('inf'):
        #     return -1
        # else:
        #     return minCoins

