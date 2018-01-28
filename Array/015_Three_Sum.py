"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
[-1, 0, 1],
[-1, -1, 2]
]

"""


class Solution(object):

    #    def threeSum(self, nums):
    #        """
    #            :type nums: List[int]
    #            :rtype: List[List[int]]
    #            """
    def threeSum(self, nums):
        nums.sort()
        ans=[]
        for l in range(0,len(nums)-2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            i = l+1
            r = len(nums)-1
            while i<r and i>l:
                temp_sum = nums[l] + nums[r] + nums[i]
                if temp_sum == 0:
                    a=[nums[l],nums[i],nums[r]]
                    ans.append(a)
                    # This will cause Time Limit Exceeded!
                    # if a not in ans: ans.append(a)
                    i += 1
                elif temp_sum > 0:
                    r -= 1
                else:
                    i += 1
        return list(set(tuple(a) for a in ans))
