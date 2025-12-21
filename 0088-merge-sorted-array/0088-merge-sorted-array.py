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
        i,j=0,0
        ans=[]
        while i<m and j <n:
            if(nums1[i]<=nums2[j]):
                ans.append(nums1[i])
                i=i+1
            else:
                ans.append(nums2[j])
                j=j+1
        while i < m:
            ans.append(nums1[i])
            i += 1

        while j < n:
            ans.append(nums2[j])
            j += 1

        # inplace replacing
        for k in range(m+n):
            nums1[k]=ans[k]
        
        return nums1
