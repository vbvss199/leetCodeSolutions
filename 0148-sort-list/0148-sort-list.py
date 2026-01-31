# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self,list1,list2) -> OptinalNode[ListNode]:
        dummyNode=ListNode(-1)
        temp=dummyNode
        while(list1!=None and list2!=None):
            if(list1.val<list2.val):
                temp.next=list1
                temp=list1
                list1=list1.next
            else:
                temp.next=list2
                temp=list2
                list2=list2.next
        if(list1):
           temp.next=list1
        if(list2):
            temp.next=list2
        return dummyNode.next
    def findMiddle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
#     def merge(self,nums,start,mid,end):
#         temp=[]
#         i=start
#         j=mid+1
#         while((i<=mid) and (j<=end)):
#             if nums[i]<=nums[j]:
#                 temp.append(nums[i])
#                 i=i+1
#             else:
#                 temp.append(nums[j])
#                 j=j+1
#         while(i<=mid):
#             temp.append(nums[i])
#             i=i+1
#         while(j<=end):
#             temp.append(nums[j])
#             j=j+1
#         for k in range(len(temp)):
#             nums[start+k]=temp[k]
#         # return nums
        
#     def mergesort(self,nums,start,end):
#         if (start < end):
#             mid=(start+end)//2
#             self.mergesort(nums,start,mid)
#             self.mergesort(nums,mid+1,end)
#             self.merge(nums, start, mid, end)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # optimal one
        if (head is None or head.next is None):
            return head
        middle =self.findMiddle(head)
        left_head =head
        right_head =middle.next 
        #as we need to separate the linked lists so we need to separate them in the sense we need to make the right to point null 
        middle.next=None #*******STAR STEP ********* make the left half and right half separated !!!!!
        left_head=self.sortList(left_head)  #as we already broken the middle link theres no point to provide the mid again 
        right_head=self.sortList(right_head) 
        return self.mergeTwoLists(left_head,right_head)  #which returns the head 
#         if not head:
#             return None

#         # convert list → array
#         temp = head
#         li = []
#         while temp:
#             li.append(temp.val)
#             temp = temp.next
#         # sort array
#         self.mergesort(li, 0, len(li) - 1)
#         # convert array → linked list
#         dummy = ListNode(0)
#         curr = dummy
#         for val in li:
#             curr.next = ListNode(val)
#             curr = curr.next
#         return dummy.next


# # [4, 2, 1, 3]

# #         mergesort(0,3)
# #  ├─ mergesort(0,1)
# #  │   ├─ mergesort(0,0)  ← return
# #  │   ├─ mergesort(1,1)  ← return
# #  │   └─ merge(0,0,1)
# #  ├─ mergesort(2,3)
# #  │   ├─ mergesort(2,2)  ← return
# #  │   ├─ mergesort(3,3)  ← return
# #  │   └─ merge(2,2,3)
# #  └─ merge(0,1,3)


