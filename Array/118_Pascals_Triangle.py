"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):

    #    def generate(self, numRows):
    #        """
    #        :type numRows: int
    #        :rtype: List[List[int]]
    #        """

    def generate(self, numRows):
        def expand(list1):
            list2 = [1]
            list2.extend((list1[x] + list1[x + 1]) for x in range(len(list1) - 1))
            list2.extend([1])
            return list2

        temp = [1]
        result = []
        for i in range(numRows):
            result.append(temp)
            temp = expand(temp)

        return result

    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0: return [1]
    result = [0] * (rowIndex+1)
    result[:rowIndex] = getRow(rowIndex - 1)
    result[1:] =  result[1:] + getRow(rowIndex - 1)
    print(result)
    return result

getRow(5)