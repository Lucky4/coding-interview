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
#
#
# 一个同时获得公共子序列的写法。
#
# public char[] LCS(String s1, String s2) {
#     int s1_length = s1.length();
#     int s2_length = s2.length();
#     int[][] dp = new int[s1_length + 1][s2_length + 1];

#     for (int i = 1; i <= s1_length; i++) {
#         for (int j = 1; j <= s2_length; j++) {
#             if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
#                 dp[i][j] = dp[i - 1][j - 1] + 1;
#             } else {
#                 dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
#             }
#         }
#     }

#     int start = 0;
#     int res_length = s1_length > s2_length ? s1_length : s2_length;
#     char[] res = new char[res_length];

#     for (int i = 1; i < dp.length; i++) {
#         for (int j = 1; j < dp[0].length; j++) {
#             if (dp[i][j] > start) {
#                 res[start] = s1.charAt(i - 1);
#                 start += 1;
#                 break;
#             }
#         }
#     }

#     return res;
# }