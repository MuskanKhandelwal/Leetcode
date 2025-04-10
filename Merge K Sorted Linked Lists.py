Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        for i in range(1,len(lists)):
            lists[i]=self.mergeList(lists[i-1],lists[i])
        return lists[-1]
    def mergeList(self, l1, l2):
        dummy =Node= ListNode()
        
        while l1 and l2:
            if l1.val<l2.val:
               Node.next=l1
               l1=l1.next
            else:
                Node.next=l2
                l2=l2.next
            Node=Node.next
        if l1:
            Node.next=l1
        else:
            Node.next=l2
        return dummy.next
