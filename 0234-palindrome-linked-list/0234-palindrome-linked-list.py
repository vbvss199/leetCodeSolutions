# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,right:Optional[ListNode]) ->Optional[ListNode]:
        prev=None
        current=right
        while(current!=None):
            nxt=current.next #save the next pointer while it is overided 
            current.next=prev #reverse the pointers 
            prev=current   #move the previous pointer 
            current=nxt #increment the current pointer
        return prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # main idea is to compare the both halves 
        slow=head
        fast=head
        # if odd length slow points at middle and fast point at the second half of the middle 
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        # now compare from left=head and reverse of slow 
        left=head
        right=self.reverse(slow)

        # now right the logic to comapre both the halves
        while(right!=None):
            if left.val!=right.val:
                return False
            right=right.next
            left=left.next
        return True
