"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.


"""

class Solution(object):


    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # only for 9 + 1  = 10
        digits.insert(0,1)
        return digits

    def plusOne(self, digits):
        # read the array as an integer, add 1, and then read new number into array again
        num = reduce(lambda x, y: x * 10 + y, digits) + 1
        return [int(i) for i in str(num)]