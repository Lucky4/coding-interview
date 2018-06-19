# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        first_k = self.GetFirstK(data, k, 0, len(data) - 1)
        last_k = self.GetLastK(data, k, 0, len(data) - 1)
        if first_k != -1 and last_k != -1:
            return last_k - first_k + 1
        return 0

    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) / 2
        if data[mid] < k:
            return self.GetFirstK(data, k, mid + 1, end)
        elif data[mid] > k:
            return self.GetFirstK(data, k, start, mid - 1)
        elif mid - 1 >= 0 and data[mid - 1] == k:
            return self.GetFirstK(data, k, start, mid - 1)
        else:
            return mid

    def GetLastK(self, data, k, start, end):
        while start <= end:
            mid = (start + end) / 2
            if data[mid] < k:
                start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            elif mid + 1 < len(data) and data[mid + 1] == k:
                start = mid + 1
            else:
                return mid
        return -1


# 注意:
#
# 1. 写程序要灵活,我一开始的想法是先这般查找,找到k后,在向左向右找k,统计个数.但是这样一点也不简洁,如果直接找到左右两边的first_k和last_k一做差加一就ok了.
# 2. 折半查找的递归形式要会写.
# 3. 要注意找不到的时候的边界情况.