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


d = Solution()
print(d.shortestPalindrome("abcd"))

c = [0, 0, 1, 1, 0, 1, 1, 2, 3]
s = "abcd"
print(s[3:][::-1])
