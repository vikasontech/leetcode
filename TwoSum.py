
# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map =  {}
        ans = []
        for i in range(len(nums)):
            if (target- nums[i] ) in map:
                ans.append(map.get(target- nums[i]))
                ans.append(i)
                return ans
            map[nums[i]] = i
        return ans
s = Solution()
# print( s.twoSum([2,7,11,15], 9) )
print( s.twoSum([3,2,4], 6) )
# print( s.twoSum([3,3], 6) )