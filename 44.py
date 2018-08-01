class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        num_word1 = len(word1)
        num_word2 = len(word2)
        dp = [[0] * (num_word2+1) for i in range(num_word1+1)]
        for i in range(1, num_word1+1):
            for j in range(1, num_word2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return num_word1 + num_word2 - 2 * dp[num_word1][num_word2]