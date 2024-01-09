# this question asks us to merge two sorted arrays
# with out creating a new array
# example: nums1 = [1,2,3,0,0,0]  m = 3  and  nums2[2,5,6]  n = 3
# the solution is going to be  [1,2,2,3,5,6]
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        last = m + n -1
        while m and n:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n -1, last - 1