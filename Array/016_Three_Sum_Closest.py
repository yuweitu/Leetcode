"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""


class Solution(object):
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for l in range(0,len(nums) -2):
            i=l+1
            r=len(nums)-1
            while i < r:
                curr=nums[l]+nums[r]+nums[i]
                if abs(target - curr) < abs(target - res):
                    res  = curr
                if curr > target:
                    r-=1
                else:
                    i+=1
        return res









    
