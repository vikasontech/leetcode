# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    wl, wr, ml= 0,0,0
    unique = set()
    i = 0
    a = list(s)

    while wr < len(s):
      while (a[wr] in unique):
        unique.remove(a[wl])
        wl += 1
      unique.add(a[wr])
      ml = max(ml, wr-wl+1)
      wr += 1

    return ml


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
