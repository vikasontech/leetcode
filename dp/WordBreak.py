# https://leetcode.com/problems/word-break/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(w) for w in wordDict) if wordDict else 0
        dp = [False] * (len(s) + 1)
        dp[0] = True # Empty string is valid base case

        for i in range(1, len(s) + 1):
            # Look back from i, but only as far as the longest word
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                print(i-1, max(i - max_len - 1, -1))
                substring = s[j:i]
                if dp[j] and substring in word_set:
                    print(f"Match found! Substring '{substring}' from index {j} to {i}")
                    dp[i] = True
                    break # We found one valid way to reach 'i', move to i+1

        return dp[len(s)]


s = Solution()
# print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# print(s.wordBreak("applepenapple", ["apple","pen"]))
print(s.wordBreak("leetcode", ["leet", "code"]))
