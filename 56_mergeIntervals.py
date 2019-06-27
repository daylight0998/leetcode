#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def merge(self, intervals):
        res = []
        for i in sorted(intervals, key=lambda i: i[0]):
            print(i[0])
            print(res)
            print("=====")

            if res and i[0] <= res[-1][1]:
                print(res[-1][1])

                res[-1][1] = max(i[1], res[-1][1])
            else:
                res += [i]
        return res


s = Solution()
print(s.merge([[1, 4], [2, 4], [4, 5]]))
