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
        # arr1 = []
        # arr1 += []
        # print(arr1)
        arr = [[1, 5], [3, 7]]
        arr[-1][1:] = 9,    # 9 是数值不具备迭代能力，需要写成 9,  而 String字符串本身在python里就是一个字符数组，是可以进行迭代操作的
        # arr[-1][-1] = 9
        print(arr)
        # print(arr[-1][-1])
        # print(arr[-1][1:])

        # print(nums[:-1])
        # print(nums[-1:])
        # print(nums[::-1])
        for n in nums:
            # print(ranges)
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            print('===')
            print(ranges)
            ranges[-1][1:] = n,
            print(ranges[-1][1:])
        return ['->'.join(map(str, r)) for r in ranges]


s = Solution()
print(s.summaryRanges([1, 2, 3, 4]))



