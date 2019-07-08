"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):

    # Data Structure: Stack
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        symbol_dict = {'}':'{', ')':'(',']':'['}
        for element in s:
            if element in '{[(':
                st.append(element)
            elif element in '}])':
                # The order of 'OR'
                if st == [] or st.pop() != symbol_dict[element]:
                    return False
            else:
                return False
        return st == []