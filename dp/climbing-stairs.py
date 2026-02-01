# https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=oizxjoit
# https://www.youtube.com/watch?v=Y0lT9Fck7qI

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

s = Solution()
print(s.climbStairs(5))