# -*- coding: utf-8 -*-
class Solution(object):
    '''
    八皇后问题，使用元组保存状态，state[0]==3,表示第1行的皇后是在第四列。
    '''
    def queens(self, num=8, state=()):
        if len(state) == num - 1:
            for pos in range(num):
                if not self.conflict(state, pos):
                    yield (pos,)
        else:
            for pos in range(num):
                if not self.conflict(state, pos):
                    for result in self.queens(num, state + (pos,)):
                        yield (pos,) + result

    def conflict(self, state, nextX):
        nextY = len(state)
	for i in range(nextY):
            if abs(state[i] - nextX) in (0, nextY - i):
	        return True
	return False


s = Solution()
print list(s.queens(8))
