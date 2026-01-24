# https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=oizxjoit
import Utilities
# https://www.youtube.com/watch?v=cRBSOz49fQk
# https://www.youtube.com/watch?v=jzZsG8n2R9A&t=30s
class Solution:
    def twoSum(self, nums: list[int], i: int) -> list[int]:
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            while nums[left] == nums[i]:
                left += 1
            while nums[right] == nums[i]:
                right -= 1

            if sum == 0:
                return [nums[i], nums[left], nums[right]]
            elif sum > 0:
                right -= 1
            else:
                left += 1
        return []


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) ==0:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            two_sum = self.twoSum(nums, i)
            if two_sum:
                res.append(two_sum)
        return res

s = Solution()
# print(s.threeSum([-3,3,4,-3,1,2]))
print(s.threeSum([-1,0,1,2,-1,-4]))
# print(s.threeSum([0,1,1]))
# print(s.threeSum([0,0,0]))
