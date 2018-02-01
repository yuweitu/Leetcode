"""
Write a function to find the longest common prefix string amongst an array of strings.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len([len(s) for s in strs]) == 0:
            return ""
        else:
            min_length  = min([len(s) for s in strs])
            n = 0
            while n < min_length:
                temp = strs[0][n]
                for i in range(len(strs)):
                    if strs[i][n] != temp:
                        return strs[0][:n]
                n += 1
            return strs[0][:n]


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(['aa','ab']))