# -*- coding:utf-8 -*-
class Solution:
    def printMatrix(self, matrix):
        cols = len(matrix[0])
        rows = len(matrix)
        if cols <= 0 or rows <= 0:
            return []
        
        start = 0
        res = []
        while cols > start * 2 and rows > start * 2:
            self.printCircle(matrix, cols, rows, start, res)
            start += 1
            
        return res
            
    def printCircle(self, matrix, cols, rows, start, res):
        endX = cols - 1 - start
        endY = rows - 1 - start
        
        for i in range(start, endX+1):
            res.append(matrix[start][i])
            
        if start < endY:
            for i in range(start+1, endY+1):
                res.append(matrix[i][endX])
                
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                res.append(matrix[endY][i])
                
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                res.append(matrix[i][start])