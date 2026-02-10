# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if not head or not head.next or k == 0:
            return head
        # find the tail
        tail=head
        len=1
        while(tail!=None and tail.next!=None):
            tail=tail.next
            len=len+1
        # connect the tail next to head
        tail.next=head

        # find the modulus of k
        k=k%len
        if(k==0):
            tail.next=None
            return head
        # now traverse till len-k then make the connections
        temp=head
        steps = len - k - 1
        while(steps>0):
            temp=temp.next
            steps=steps-1
        head=temp.next
        temp.next=None

        return head
