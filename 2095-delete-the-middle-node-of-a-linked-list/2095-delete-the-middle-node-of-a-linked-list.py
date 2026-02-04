# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        #we have the middle pointer now remove this link and move the connection ?
        temp=head
        if not head or not head.next:
            return None
        while(temp!=None and temp.next!=None):
            if(temp.next==slow):
                temp.next=slow.next
                break
            else:
                temp=temp.next
        return head
        