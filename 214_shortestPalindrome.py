#!/usr/bin/python3
# encoding: utf-8


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        A = s + "*" + s[::-1]
        print(A)
        cont = [0]
        for i in range(1, len(A)):
            index = cont[i - 1]
            print(A[index]+" : "+A[i])
            while index > 0 and A[index] != A[i]:
                index = cont[index - 1]
            cont.append(index + (1 if A[index] == A[i] else 0))
            print(cont)
        return s[cont[-1]:][::-1] + s


# d = Solution()
# print(d.shortestPalindrome("abcd"))
#
# c = [0, 0, 1, 1, 0, 1, 1, 2, 3]
# s = "abcd"
# print(s[3:][::-1])


class S:
    def shortestPalindrome1(self, g):
        s = g + "|" + g[::-1]
        lps = [-1] + [0] * len(s)
        print(s)
        print(lps)
        print("=========")
        l, r = -1, 0
        while r < len(s):
            while l >= 0 and s[l] != s[r]:
                l = lps[l]
            l, r = l + 1, r + 1
            lps[r] = l
        print(lps)
        print(lps[-1])
        print(g[lps[-1]:][::-1])
        return g[lps[-1]:][::-1] + g


s = S()
print(s.shortestPalindrome1("abcd"))
