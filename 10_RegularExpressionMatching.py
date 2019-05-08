#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return not s.isalpha()
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')
        if p[1] != '*':
            if len(s) == 0:
                return False
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        while len(s) != 0 and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])


s = Solution()
# print(s.isMatch("ab", "a**b"))
# print(s.isMatch("mississippi", "mis*is*p*."))
# print(s.isMatch("aab", "c*a*b"))
# print(s.isMatch("abcd", "d*"))
print(s.isMatch("dd", "d*"))
# print(not ''.isalpha())


# a = tuple([1, 2, 3, 4])
# b = tuple({1: 2, 3: 4})
# print(a)
# print(b)
