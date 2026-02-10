# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # deleting all the duplicate nodes of the linked list 
        # if the current and current.next are equal then remove both the links 
        temp=head
        prev=None
        while(temp!=None and temp.next!=None):
            if(temp.val==temp.next.val):
                dup_val=temp.val
                # need to remove the links where the values are same else just traverse the link 
                # check if it is head then we need to move the head
                # here we need to remove the link for the temp as well then we able to pull up the logic !   
                # check if it is head
                while temp and temp.val==dup_val:
                    temp=temp.next
                if prev is None:
                    head=temp
                else:
                    prev.next=temp
            else:
                prev=temp
                temp=temp.next
        return head 
