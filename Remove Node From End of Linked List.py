Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        tmp1=head
        while tmp1:
            count+=1
            tmp1=tmp1.next
        if n == count:
            return head.next
        tmp = head
        for _ in range(count - n - 1):
            tmp = tmp.next

        tmp.next = tmp.next.next
        return head
