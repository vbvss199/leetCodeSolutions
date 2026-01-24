# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        li=[]
        while(temp1!=None):
            li.append(temp1.val)
            temp1=temp1.next
        while(temp2!=None):
            li.append(temp2.val)
            temp2=temp2.next
        li.sort()
        dummy_node=ListNode(0)
        current=dummy_node
        for i in range(len(li)):
            current.next=ListNode(li[i])
            current=current.next
        return dummy_node.next