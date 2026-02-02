# https://leetcode.com/problems/longest-consecutive-sequence/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ns = set(nums)
        longest = 0
        for num in ns:
            if num-1 not in ns:
                length = 1
                while (num+length) in ns:
                    length += 1
                longest = max(length, longest)
        return longest


s = Solution()
assert 5 == s.longestConsecutive([100,4,200,1,3,2, 0]), '1'
assert 9 == s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), '2'
assert 3 == s.longestConsecutive([1,0,1,2]), '3'
assert 2 == s.longestConsecutive([0,-1]), '4'
assert 1 == s.longestConsecutive([0]), '5'

