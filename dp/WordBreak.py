# https://leetcode.com/problems/word-break/?envType=problem-list-v2&envId=oizxjoit
from importlib.util import source_hash


class Solution:
    def printArray(self, s: str):
        # Header row (indexes)
        header = "| " + " | ".join(str(i) for i in range(len(s))) + " |"

        # Character row
        chars = "| " + " | ".join(c for c in s) + " |"

        print(header)
        # print(separator)
        print(chars)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.printArray(s)
        wordSet = set(wordDict)
        maxLen = max(len(w) for w in wordSet) if wordDict else None
        dp = [False] * (len(s) + 1)
        dp[0] = True
        print(dp)
        print(s)
        print(maxLen)
        for i in range(len(s) + 1):
            for j in range(i - 1, max(i - maxLen - 1, -1), -1):
                substring = s[j:i]
                if dp[j] and substring in wordSet:
                    dp[i] = True
                    break
        print(dp)
        return dp[len(s)]


s = Solution()
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# print(s.wordBreak("applepenapple", ["apple","pen"]))
# print(s.wordBreak("leetcode", ["leet", "code"]))
