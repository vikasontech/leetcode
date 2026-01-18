# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
from ipaddress import summarize_address_range
from os import umask


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = numbers
        left, right = 0, len(n)-1
        while left <= right:
            sum = n[left] + n[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,4], 6))
print(s.twoSum([-1,0], -1 ))
