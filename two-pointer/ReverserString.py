"""
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, ll: ListNode) -> ListNode:
        head = ll
        



s = Solution()
head = node = ListNode(1)
for i in range(2, 5):
    while node.next != None:
        node = node.next
    node.next = ListNode(i)

print(head)
# print(node)
s.reverseList(head)
