from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeContainer = {}

        def clone(self, node) -> 'Node':
            if (node in nodeContainer):
                return node
            copy = Node(val=node.val)
            nodeContainer[node] = copy
            for ne in node.neighbors:
                copy.neighbors.append(clone(ne))

            return copy

        return clone(node) if node else None

sol = Solution()
sol.cloneGraph()