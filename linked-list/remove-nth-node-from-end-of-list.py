# https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=oizxjoit
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # set the right pointer
        while n > 0 and right:
            right = right.next
            n-=1

        # When this loop finish, the left pointer would be on the n-1 node
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


s = Solution()
s.removeNthFromEnd(None, 0)