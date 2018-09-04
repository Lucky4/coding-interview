# -*- coding:utf-8 -*-


class LCS:
    def findLCS(self, A, n, B, m):
        dp = [[0] * (m + 1) for i in range(n + 1)] # 注意这里，不要用列表乘法定义二维数组
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]


# 注意，不要使用列表乘法定义二维数组，如[[0] * (m+1)] * (n+1)的方式定义的。因为乘法只是简单的创建了Array引用，其中某个改变会引起其他改变。
# 参考：https://github.com/CyC2018/Interview-Notebook/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3.md#%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97
