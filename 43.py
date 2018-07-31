class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        num_prices = len(prices)
        buy = [0] * num_prices
        s1 = [0] * num_prices
        sell = [0] * num_prices
        s2 = [0] * num_prices
        buy[0] = s1[0] = -prices[0]
        sell[0] = s2[0] = 0
        for i in range(1, num_prices):
            buy[i] = s2[i-1] - prices[i]
            s1[i] = max(s1[i-1], buy[i-1])
            sell[i] = max(buy[i-1], s1[i-1]) + prices[i]
            s2[i] = max(s2[i-1], sell[i-1])
        return max(sell[num_prices-1], s2[num_prices-1])

# 针对每天的股价有4种行为，每个行为都用一个状态来表示，每个状态都由之前的状态转换而来。
# 参考：https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E8%82%A1%E7%A5%A8%E4%BA%A4%E6%98%93