class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s=''.join([char.lower() for char in s if char.isalnum()])
        for i in range(len(cleaned_s) // 2):
         if cleaned_s[i]!=cleaned_s[-(i+1)]:
           return  False
        return True

        