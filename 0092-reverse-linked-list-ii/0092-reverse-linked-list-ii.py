# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        # using the dummy nodes 
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        for _ in range(left-1):
            prev=prev.next
            # after this prev will point to the the position before left 
        
        curr=prev.next
        for _ in range(right-left):
            nxt=curr.next
            curr.next=nxt.next #pointers reveresed 
            nxt.next=prev.next
            prev.next=nxt
        return dummy.next