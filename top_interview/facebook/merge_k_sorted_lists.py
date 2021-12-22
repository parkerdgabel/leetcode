# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional
from functools import reduce


def merge2lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    while True:
        if a is None:
            tail.next = b
            break
        if b is None:
            tail.next = a
            break
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    return dummy.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return reduce(merge2lists, lists) if len(lists) > 0 else None
