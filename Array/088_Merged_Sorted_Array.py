"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

"""

class Solution(object):

#    def merge(self, nums1, m, nums2, n):
#       """
#        :type nums1: List[int]
#        :type m: int
#        :type nums2: List[int]
#        :type n: int
#        :rtype: void Do not return anything, modify nums1 in-place instead.
#       """
    def merge(self, nums1, m, nums2, n):
        # Wrong Solution!!!
        # it is wrong to start from the beginning, because it may re-write original nums1.
        m_pointer = 0
        n_pointer = 0
        while n_pointer < n and m_pointer < m:
            if nums1[m_pointer] <= nums2[n_pointer]:
                nums1[m_pointer + n_pointer] = nums1[m_pointer]
                m_pointer += 1
            else:
                nums1[m_pointer + n_pointer] = nums2[n_pointer]
                n_pointer += 1
        if n_pointer < n:
            nums1[m + n_pointer:] = nums2[n_pointer:]
        if m_pointer < m:
            nums1[n + m_pointer:] = nums1[m_pointer:]
        return

    def merge(self, nums1, m, nums2, n):
        # Starting from the tail is the right way
        m_pointer = m - 1
        n_pointer = n - 1
        pos = m + n - 1

        while n_pointer >= 0 and m_pointer >= 0:
            if nums1[m_pointer] >= nums2[n_pointer]:
                nums1[pos] = nums1[m_pointer]
                m_pointer -= 1
            else:
                nums1[pos] = nums2[n_pointer]
                n_pointer -= 1
            pos -= 1
        while n_pointer >= 0:
            nums1[pos] = nums2[n_pointer]
            n_pointer -= 1
            pos -= 1

        return

    def merge(self, nums1, m, nums2, n):
        # finish with python slicing
        m_pointer, n_pointer, pos = m - 1, n - 1, m + n - 1

        while n_pointer >= 0 and m_pointer >= 0:
            if nums1[m_pointer] >= nums2[n_pointer]:
                nums1[pos] = nums1[m_pointer]
                m_pointer -= 1
            else:
                nums1[pos] = nums2[n_pointer]
                n_pointer -= 1
            pos -= 1

        if n_pointer >= 0:
            nums1[:pos + 1] = nums2[:n_pointer + 1]

        return


