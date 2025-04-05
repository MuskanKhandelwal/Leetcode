Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val=[]
        while head.next:
            val.append(head.val)
            print(val)
            head=head.next
            if head.next and (head.next.val in val):
                return True
                break
        return False

        
