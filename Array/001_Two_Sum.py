"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution(object):

    #    def twoSum(self, nums, target):
    #        """
    #        :type nums: List[int]
    #        :type target: int
    #        :rtype: List[int]
    #        """

    def twoSum(self, nums, target):
        # Time limit exceeded
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
    def twoSum(self, nums, target):
        # Two Pointers Methods
        num_index = [(value, index)for index, value in enumerate(nums)]
        num_index.sort()
        begin, end = 0, len(nums) -1
        while begin < end:
            curr = num_index[begin][0] + num_index[end][0]
            if curr == target:
                return [num_index[begin][1], num_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

    def twoSum(self, nums, target):
        # Hash Table 1
        # build hash table
        hash_nums={}
        for index,value in enumerate(nums):
            try:
                hash_nums[value].append(index)
            except:
                hash_nums[value] = [index]

        # search
        for index,value in enumerate(nums):
            another = target - value
            try:
                if index != hash_nums[another][0]:
                    return [index, hash_nums[another][0]]
            except:
                pass

    def twoSum(self, nums, target):
        # Hash Table 2
        hash_nums={}
        for index,value in enumerate(nums):
            if target - value in hash_nums:
                return [index, hash_nums[target-value]]
            # this line is after 'if', to avoid using the same element twice
            hash_nums[value]=index

