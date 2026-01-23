# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # given two linked listsl1 and l2 
        temp1=l1
        temp2=l2
        var1=''
        var2=''
        while(temp1!=None):
            var1=var1+str(temp1.val)
            temp1=temp1.next
        while(temp2!=None):
            var2=var2+str(temp2.val)
            temp2=temp2.next
        k=int(var1[::-1]) + int(var2[::-1])
        dummy = ListNode(0)
        curr = dummy

        for ch in str(k)[::-1]:
            curr.next = ListNode(int(ch))
            curr = curr.next

        return dummy.next