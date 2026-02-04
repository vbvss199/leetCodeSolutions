# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,slow:Optional[ListNode]) -> None:
        curr=slow
        prev=None
        while(curr!=None):
            # save the next pointer
            nxt=curr.next

            # reverse the pointer directions 
            curr.next=prev

            # interchange the current and preious
            prev=curr

            # reassign the nxt pointer to current
            curr=nxt
        return prev 

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # swap logic between the last element and the first element and move the first pointer!!!
        if not head or not head.next:
            return
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        # reverse the list from slow and merge alternatively
        right=self.reverseList(slow.next)
        # cut the link
        slow.next=None
        left=head

        # now merge both the right and left alternatively 
        while(right!=None):
            rightnext=right.next
            leftnext=left.next

            left.next=right

        #   after the first iteration the link looks like [1,5] [2,3] and [4]
        # so here we need to connect [1,5] with [2,3 ] 5 to 2 whcih is right.next and left.next 
            right.next=leftnext

            left=leftnext
            right=rightnext
        return head

