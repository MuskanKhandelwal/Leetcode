# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nexti = None
        while curr:
            nexti = curr.next 
            curr.next = prev
            prev = curr
            curr = nexti
        return prev


#Need 3 pointers for the solution prev, curr, next 
