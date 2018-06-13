# -*- coding:utf-8 -*-


class Find:
    # array 二维列表
    def method1(self, target, array):
        row = len(array)-1
        col = 0
        
        while row >= 0 and col <= len(array[0])-1:
            if array[row][col] < target:
                col += 1
            elif array[row][col] > target:
                row -= 1
            else:
                return True
        
        return False

    def method2(self, target, array):
        for i in array:
            low = 0
	    high = len(i) - 1
	    while low <= high:
                mid = (low + high) / 2
		if i[mid] < target:
                    low = mid + 1
	        elif i[mid] > target:
		    high = mid - 1
		else:
		    return True

	 return False
