#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)
        a = 0
        b = 0
        if ls < len(p):
            return 0
        while a < ls:
            if b < lp and (s[a] == p[b] or p[b] == "?"):
                a = a+1
                b = b+1
            elif b < lp and p[b] == '*':
                a = a+1
                if b+1 < lp and s[a] == p[b+1]:
                    b = b+1
            elif p[lp-1] == '*':
                return 1
            else:
                return 0
        return 1


d = Solution()
print(d.isMatch('abbab', 'a*ab'))
