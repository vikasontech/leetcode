# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    '''
    complexity O(n) and space O (n)
    '''
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False

    '''
    complexity O(nlogn) because of sorting and space O(1)
    '''
    def containsDuplicate2(self, nums: list[int]) -> bool:
        length = len(nums)
        if(length == 0 or length == 1):
            return False

        nums.sort()
        l,r = 0,1
        while r < length:
            if nums[l] == nums[r]:
                return True
            r += 1
            l += 1

        return False


s = Solution()

assert s.containsDuplicate([1,2,3,1]), '1'
assert not s.containsDuplicate([1,2,3]), '2'
assert not s.containsDuplicate([9]), '3'
assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), '4'
