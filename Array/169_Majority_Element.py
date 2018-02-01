"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

This is an important question with various solutions!!
"""
import collections

class Solution(object):
#    def majorityElement(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: int
#        """
    def majorityElement(self, nums):
        nums_dict = {}
        for num in nums:
            try:
                nums_dict[num] += 1
            except:
                nums_dict[num] = 1
        for num in nums_dict.keys():
            if nums_dict[num] > len(nums)/2:
                return num



    def majorityElement(self, nums):
        # Hash Table
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement(self, nums):
        # Sorting
        nums.sort()
        return nums[len(nums)//2]


