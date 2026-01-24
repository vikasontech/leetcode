# https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=oizxjoit
# https://www.youtube.com/watch?v=jzZsG8n2R9A
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # [-4,-1,-1,0,1,2]
        nums.sort()
        res = []
        i = 0
        # while i < len(nums):
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue;
            if nums[i] > 0:
                continue
            if len(nums) == 3 and nums[0] > 0:
                continue
            # Apply two sum II here
            left, right = i+1, len(nums) - 1
            while left < right  :
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    # Handle duplicates
                    res.append([nums[i] , nums[left] , nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            i += 1
        return res;
s = Solution()

print(s.threeSum([-3,-3,4,3,2,1]))
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,1,1]))