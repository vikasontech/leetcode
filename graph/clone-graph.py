# https://leetcode.com/problems/clone-graph/?envType=problem-list-v2&envId=oizxjoit
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def cloneDfs(node: Node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(val= node.val)
            oldToNew[node] = copy

            for ne in node.neighbors:
                copy.neighbors.append(cloneDfs(ne))

            return copy

        return cloneDfs(node)

s = Solution()
s.cloneGraph(None)

