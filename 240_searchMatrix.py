#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lm = len(matrix)
        if lm <= 0:
            return False
        ll = len(matrix[0])
        if ll <= 0:
            return False
        if matrix[0][0] > target or matrix[lm-1][ll-1] < target:
            return False
        x = lm - 1
        y = 0
        while True:
            if matrix[x][y] < target:
                y = y + 1
            elif matrix[x][y] > target:
                x = x - 1
            else:
                return True
            print(x, ' : ', y)
            if x < 0 or y > ll - 1:
                break
        return False


m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
k = [[]]
t = [[-1], [-1]]
n = [[1],
     [3],
     [5]]
s = Solution()
print(s.searchMatrix(n, 2))
