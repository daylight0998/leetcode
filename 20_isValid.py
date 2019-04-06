#!/usr/bin/python3
# encoding: utf-8

# Input: "([)]"
# Output: false
# Input: "{[]}"
# Output: true
# Input: "{}[]()"
# Output: true

# st = '0123456789'
# print(st[0:3]) #截取第一位到第三位的字符
# print str[:] #截取字符串的全部字符
# print str[6:] #截取第七个字符到结尾
# print str[:-3] #截取从头开始到倒数第三个字符之前
# print str[2] #截取第三个字符
# print str[-1] #截取倒数第一个字符
# print str[::-1] #创造一个与原字符串顺序相反的字符串
# print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
# print str[-3:] #截取倒数第三位到结尾
# print str[:-5:-3] #逆序截取,


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        else:
            return self.valid(s)

    def valid(self, s: str):
        ls = len(s)
        arr = ['(', ')', '[', ']', '{', '}']
        for i in range(1, ls):
            if s[i] in (arr[1], arr[3], arr[5]):
                # print(s[i])
                if s[i] == arr[1]:  # ()
                    if s[i-1] != arr[0]:
                        return False
                    else:
                        if i - 1 == 0:
                            s1 = ''
                        else:
                            s1 = s[0:i - 1]
                        print(s1)
                        s1 += s[i + 1:]
                        print(s1)
                        if len(s1) == 0:
                            return True
                        self.isValid(s1)
                if s[i] == arr[3]:  # []
                    if s[i-1] != arr[2]:
                        return False
                    else:
                        if i - 1 == 0:
                            s1 = ''
                        else:
                            s1 = s[0:i - 1]
                        print(s1)
                        s1 += s[i + 1:]
                        print(s1)
                        if len(s1) == 0:
                            return True
                        self.isValid(s1)
                if s[i] == arr[5]:  # {}
                    if s[i-1] != arr[4]:
                        return False
                    else:
                        if i - 1 == 0:
                            s1 = ''
                        else:
                            s1 = s[0:i - 1]
                        print(s1)
                        s1 += s[i + 1:]
                        print(s1)
                        if len(s1) == 0:
                            return True
                        self.isValid(s1)
        return True


s = Solution()
# print(s.isValid("{}[]()"))
print(s.isValid("{[]}"))




