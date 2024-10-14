# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 
# Example 1:
# Input: columnNumber = 1
# Output: "A"
# Example 2:
# Input: columnNumber = 28
# Output: "AB"
# Example 3:
# Input: columnNumber = 701
# Output: "ZY"


# While Loop:
# We continuously process the columnNumber by subtracting 1 and then taking the modulus 26 to determine the current letter. The result is added to a list.
# The list stores the letters in reverse order, so we reverse it at the end.

# chr() and ord():
# chr() is used to convert an integer to its corresponding character.
# ord('A') gives the ASCII value of 'A', so remainder + ord('A') gives the correct character.


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            reminder =  columnNumber % 26
            ans.append(chr(reminder + ord('A')))
            columnNumber //= 26

        return ''.join(reversed(ans))
        
