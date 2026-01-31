# https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=oizxjoit
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2= list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next

s = Solution()
# list1 = ListNode(2, ListNode(2, ListNode(3, ListNode(5))))
# list2 = ListNode(1, ListNode(2, ListNode(4)))


list1 = ListNode(0)
list2 = ListNode(1 , ListNode(2, ListNode(3, ListNode(5))))

list1 = ListNode(1 , ListNode(2, ListNode(4)))
list2 = ListNode(1 , ListNode(3, ListNode(4)))

list1 = None
list2 = ListNode()

list1 = ListNode(5)
list2 = ListNode(1 , ListNode(3, ListNode(4)))

result = s.mergeTwoLists(list1, list2)
while result:
    print(result.val)
    result = result.next




