#!/usr/bin/python3
# encoding: utf-8
import math


class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        for a in range(0, int(math.sqrt(n)) + 1):
            b = math.sqrt(n - a * a)
            if a * a + b * b == n and (b % int(b) == 0.0 or b % int(b) == 0):
                print(a)
                print(b % int(b) == 0.0 or b % int(b) == 0)
                return (0 if a is 0 else 1) + (1 if b % int(b) == 0.0 or b % int(b) == 0 is True else 0)
        return 3


s = Solution()
# print(s.numSquares(6))  # 3
# print(s.numSquares(1))  # 1
# print(s.numSquares(12))  # 3
# print(s.numSquares(13))  # 2
# print(s.numSquares(10))  # 2
# print(s.numSquares(9))  # 1
# print(s.numSquares(14))  # 1
print(s.numSquares(15))  # 4
