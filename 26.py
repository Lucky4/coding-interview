class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        return list(self.dc(array, 0, len(array) - 1))

    def dc(self, array, start, end):
        res = set()

        if start == end:
            return set(array[start:end + 1])

        spl = (start + end) / 2
        s1 = self.dc(array, start, spl)
        s2 = self.dc(array, spl + 1, end)

        return s1.union(s2).difference(s1.intersection(s2))


# 遇到重复问题要想到使用集合
# 其他思路参考: http://zhedahht.blog.163.com/blog/static/2541117420071128950682/