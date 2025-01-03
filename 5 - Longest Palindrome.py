#Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #accessing from the centre
        def expandCentre(left, right):
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        longPal = ""
        for i in range(len(s)):
            oddPal = expandCentre(i, i)
            evenPal = expandCentre(i, i+1)
            if len(oddPal) > len(longPal):
                longPal = oddPal
            if len(evenPal) > len(longPal):
                longPal = evenPal
        return longPal
