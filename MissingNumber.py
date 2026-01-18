# https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        numsSet = set(nums)
        for i in range(len(nums)+1):
            if i not in numsSet:
                return i
        return -1

s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))