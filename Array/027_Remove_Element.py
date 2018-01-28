"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""

class Solution(object):
    #    def removeElement(self, nums, val):
    #        """
    #        :type nums: List[int]
    #        :type val: int
    #        :rtype: int
    #        """

    def removeElement(self, nums, val):
        #list.remove(value) only remove one element! Not ALL elements in the same value
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        return len(nums)

    def removeElement(self, nums, val):
        # Two Pointers Methods
        ls = len(nums)
        count = 0
        left = 0
        for i in range(0, ls):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
                count += 1
        return count