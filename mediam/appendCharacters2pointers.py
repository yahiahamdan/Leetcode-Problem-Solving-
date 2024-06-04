"""
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").

llg  g
output 0 
"""

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sIndex=0
        tIndex=0
        sLength=len(s)
        tLength=len(t)
        while sIndex < sLength and tIndex <tLength:
            if s[sIndex] == t[tIndex]:
                tIndex+=1
            sIndex+=1
        return tLength-tIndex