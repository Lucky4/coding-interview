class Solution:
    def func(self, ss, m, target):
        res = []
        subset = [0] * m
        self.combination(ss, len(ss), m, target, subset, res, target)
        return res

    def combination(self, ss, n, m, target, subset, res, k):
        for i in range(n, m-1, -1):
            if ss[i-1] > target:
                continue

            subset[m-1] = i-1

            if m > 1:
                self.combination(ss, i-1, m-1, target-ss[i-1], subset, res, k)
            else:
                tmp = 0
                for i in subset:
                    tmp += ss[i]
                if tmp == k:
                    res.append(subset[:])


print sorted(Solution().func([10, 20, 30, 10, 20, 600, 30, 70, 80, 90, 100], 3, 150))