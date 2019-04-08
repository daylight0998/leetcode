#!/usr/bin/python3
# encoding: utf-8

# nums: List[int]
# return: List[str]


class Solution:
    # def summaryRanges(self, nums):
    #     step, ln, arr = 0, len(nums), []
    #     if ln <= 1:
    #         return nums
    #     for i in range(ln - 1):
    #         if nums[i+1] - nums[i] == 1:
    #             step = step + 1
    #         elif step == 0:
    #             arr.append(nums[i])
    #         else:
    #             arr.append(nums[i - step] + "->" + nums[i])
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]


s = Solution()
print(s.summaryRanges([1, 2, 3, 4]))



