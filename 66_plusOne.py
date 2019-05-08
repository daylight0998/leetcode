#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def plusOne(self, digits):
        l = len(digits)
        for i in range(l-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne([0]))