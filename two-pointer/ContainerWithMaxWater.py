from typing import List

from setuptools.windows_support import hide_file


# https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=oizxjoit
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.

class Solutions:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height ) -1
        i=0
        maxwc = 0
        while l < r :
            minValue = min(height[l], height[r])
            wc = minValue * (len(height) - i -1 )
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
            maxwc = max(maxwc, wc)
        return maxwc

s = Solutions()
print(s.maxArea([8,8,8,34,34,44,5,6,4,81]))
# print(s.maxArea([1,8,6,2,5,4,8,3,7]))