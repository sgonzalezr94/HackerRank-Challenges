from typing import Optional

# https://leetcode.com/problems/add-two-numbers/submissions/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, value=0, next=ListNode()) -> None:
        self.head = ListNode(value)
        self.next = next

    def addNode(self, next=ListNode()):
        self.head.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = int("".join(l1))
        n2 = int("".join(l2))
        return list(n1 + n2)


tst_list = ListNode(5, 4)
# print(tst_list.val)
tst_list.next = 7

lista = LinkedList(10, tst_list)
print(lista.head)

# current = tst_list.next
# while current is not None:
#     print(current.val)
#     current = current.next
