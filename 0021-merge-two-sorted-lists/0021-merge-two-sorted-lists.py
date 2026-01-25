# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # naive solution 
        # temp1=list1
        # temp2=list2
        # li=[]
        # while(temp1!=None):
        #     li.append(temp1.val)
        #     temp1=temp1.next
        # while(temp2!=None):
        #     li.append(temp2.val)
        #     temp2=temp2.next
        # li.sort()
        # dummy_node=ListNode(0)
        # current=dummy_node
        # for i in range(len(li)):
        #     current.next=ListNode(li[i])
        #     current=current.next
        # return dummy_node.next

        # optimal solution   
        temp1=list1
        temp2=list2
        dummy=ListNode(0)
        temp=dummy
        while(temp1!=None and temp2!=None):
            if(temp1.val<temp2.val):
                temp.next=temp1
                temp=temp1
                temp1=temp1.next
            else:
                temp.next=temp2
                temp=temp2
                temp2=temp2.next
        if(temp1):
            temp.next=temp1
        else:
            temp.next=temp2
        return dummy.next
        