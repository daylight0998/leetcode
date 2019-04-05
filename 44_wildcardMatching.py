#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)
        i = 0
        j = 0
        istar = -1
        jstar = -1

        if ls < lp or lp == 0:
            return False
        while i < ls:
            if j < lp and (s[i] == p[j] or p[j] == "?"):
                i = i + 1
                j = j + 1
            elif j < lp and p[j] == '*':
                istar = i
                j = j + 1
                jstar = j
                print('jstar: %d' % jstar)
            elif istar >= 0:
                istar = istar + 1
                i = istar
                j = jstar + 1
                print('j: %d' % j)
            else:
                return False
        while j < lp and p[j] == '*':
            print(j)
            j = j + 1
        return j == lp
                # if b+1 < lp and a+1 < ls and (s[a] == p[b+1] or p[b+1] == '*'):
                #     b = b+1
                # elif b+1 < lp and a+1 < ls and (s[a] != p[b+1] or p[b+1] != '*'):
                #     return False
        #     elif p[lp-1] == '*':
        #         return True
        #     else:
        #         return False
        # return True


# d = Solution()
# print(d.isMatch("acdcb", "a*"))
# print(d.isMatch("acdcb", "a*c?b"))
# print(d.isMatch("acdcb", "a*cb"))
# print(d.isMatch("adceb", "*a*b"))


class S:
    def match(self, s: str, p: str) -> bool:
        return self.helper(s, p, 0, 0) > 1

    def helper(self, s, p, i, j):
        ls = len(s)
        lp = len(p)
        if i >= ls-1 and j >= lp-1:
            return 2    # 返回2表示成功匹配
        if i == ls and p[j] != '*':
            return 0    # 若s串匹配完成了，但p串但当前字符不是星号，返回状态0, 失败
        if j == lp:
            return 1    # 匹配结束
        if s[i] == p[j] or p[j] == '?':
            return self.helper(s, p, i + 1, j + 1)
        if p[j] == '*':
            if j + 1 < lp and p[j + 1] == '*':
                return self.helper(s, p, i, j + 1)
            for k in range(0, ls - i):
                res = self.helper(s, p, i + k, j + 1)
                if res == 0 or res == 2:
                    return res
        return 1


m = S()
print(m.match("adcebd", "?d**c*b*?"))
# print(m.match("adceb", "*a*b"))
# print(m.match("acdcb", "a*"))
