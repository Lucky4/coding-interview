# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def maxInWindows(self, num, size):
        if len(num) < 1 or size < 1: return []

        window = deque()
        for i in range(0, size - 1):
            window.append(num[i])

        res = []
        for j in range(size - 1, len(num)):
            window.append(num[j])
            res.append(max(window))
            window.popleft()

        return res