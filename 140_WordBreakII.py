#!/usr/bin/python3
# encoding: utf-8

class Solution(object):
        def wordBreak(self, s, wordDict):
            """
            :type s: str
            :type wordDict: List[str]
            :rtype: List[str]
            """
            Solution.res = []
            self.dfs(s, wordDict, '')
            return Solution.res

        def dfs(self, s, wordDict, stringlist):
            if self.check(s, wordDict):
                # 如果s已经切完，则加入最后结果集
                if len(s) == 0:
                    Solution.res.append(stringlist[1:])
                for i in range(1, len(s)+1):
                    print("==="+s[:i])
                    if s[:i] in wordDict:
                        print (stringlist+' '+s[:i])
                        self.dfs(s[i:], wordDict, stringlist+' '+s[:i])

        def check(self, s, wordDict):
                dp = [False for i in range(len(s)+1)]
                dp[0] = True
                # 这里循环是len(s)，使得该check函数变成了只要有单词在里面就验证成功，和wordbreak有所不同！
                for i in range(len(s)):
                    for j in range(i, -1, -1):
                        if dp[j] and s[j:i + 1] in wordDict:
                            dp[i + 1] = True
                            break
                return dp[len(s)]
d = Solution();
d.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]);
