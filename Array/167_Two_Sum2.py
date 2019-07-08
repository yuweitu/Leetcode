"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""

class Solution:

	# two pointers, time complexity O(nlogn), space complexity O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start, end = 0,  n -1
        while start < end :
            if numbers[start] + numbers[end] == target:
                return start + 1, end + 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return None