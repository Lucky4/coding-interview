class Solution(object):
    def coinChange(self, coins, amount):
        if not coins:
            return 0
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
                    
        if dp[amount] > amount:
            return -1
        
        return dp[amount]