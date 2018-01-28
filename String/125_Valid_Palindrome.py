"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""



class Solution(object):
#    def isPalindrome(self, s):
#        """
#        :type s: str
#        :rtype: bool
#        """
    def isPalindrome(self, s):
        # recursive method doesn't work
        alnum_s = [t.lower() for t in s if t.isalnum()]
        if len(alnum_s) < 1:
            return True
        else:
            if alnum_s[0] == alnum_s[-1]:
                return self.isPalindrome(alnum_s[1:-1])
            else:
                return False

    def isPalindrome(self, s):
        # two pointers method
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

    def isPalindrome(self, s):  
        # cut from the middle, similar to two pointers
        alnum_s = [t.lower() for t in s if t.isalnum()]
        if len(alnum_s) <= 1:
            return True
        for i in range(len(alnum_s) / 2):
            if alnum_s[i] != alnum_s[len(alnum_s) - 1 - i]:
                return False
        return True 


    def isPalindrome(self, s): 
        # python reverse list
        alnum_s = [t.lower() for t in s if t.isalnum()]
        return alnum_s == alnum_s[::-1]

    
