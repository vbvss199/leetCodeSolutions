class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # with a space of O(n) using two pointers
        # the combined array should have a length of m+n 
        # i and j can also be reffered as right and left 
        # need to go on still left <m and right <n 
        # left,right=0,0
        # ans=[]
        # while left<m and right <n:
        #     if(nums1[left]<=nums2[right]):
        #         ans.append(nums1[left])
        #         left=left+1
        #     else:
        #         ans.append(nums2[right])
        #         right=right+1
        # # after traversal above i starts from the point where it left 
        # while left < m:
        #     ans.append(nums1[left])
        #     left += 1

        # while right < n:
        #     ans.append(nums2[right])
        #     right += 1

        # # inplace replacing
        # for k in range(m+n):
        #     nums1[k]=ans[k]
        
        # return nums1


        # lets do this same question in the space complexity of O(1)
        # considering the two arrays are sorted lets do like small numbers to one array and larger numbers to one array by comparing the last element and first element of first and second array of not swap them

        left=m-1
        right=n-1
        k=m+n-1
        # ned to merge two arrays such 
        while right>=0:
            if left>=0 and nums1[left]>nums2[right]:
                nums1[k]=nums1[left]
                left=left-1
            else:
                nums1[k]=nums2[right]
                right=right-1
            k=k-1
        return nums1
        