# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=oizxjoit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # // DFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



s = Solution()
s.maxDepth(None)