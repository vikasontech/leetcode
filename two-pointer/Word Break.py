# https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=oizxjoit
# 139. Word Break
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i = 0
        l = 0
        r = 1
        alreadyFound = [""]
        val = str
        while i < len(s):
            if s[l:r] in wordDict and s[l:r] not in alreadyFound:
                val = s[l:r]
                alreadyFound.append(val)
                l = r
            r +=1
            i += 1

        return l == (r -1)


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
