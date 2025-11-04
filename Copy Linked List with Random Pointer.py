# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        maphash={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            maphash[curr]= copy
            curr=curr.next
        curr=head
        
        while curr:
            copy=maphash[curr]
            copy.next=maphash[curr.next]
            copy.random =maphash[curr.random]
            curr=curr.next
        return maphash[head]

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Oldtocopy = {None:None}

        curr = head
        while curr: #one pass
            copy = Node(curr.val)
            Oldtocopy[curr] = copy
            curr = curr.next
        curr = head

        while curr: #two pass
            copy = Oldtocopy[curr]
            copy.next = Oldtocopy[curr.next]
            copy.random = Oldtocopy[curr.random]
            curr = curr.next
        return Oldtocopy[head]
