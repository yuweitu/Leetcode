"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def expand(list1):
            list2 = [1]
            list2.extend((list1[x] + list1[x + 1]) for x in range(len(list1) - 1))
            list2.extend([1])
            return list2

        start = [1]
        result = []
        for i in range(rowIndex):
            result = expand(start)
            start = result
        return start