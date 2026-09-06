# Title: Zigzag Conversion
# Submission ID: 2133163183
# Status: Accepted
# Date: September 6, 2026 at 11:33:06 PM GMT+5:30

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Special cases: no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s

        # Create one empty string for each row
        rows = [''] * numRows

        current_row = 0
        going_down = False   # We start by going down

        for char in s:
            # Put the character in the current row
            rows[current_row] += char

            # Change direction when we hit the top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down
            if going_down:
                current_row += 1
            else:
                current_row -= 1

        # Join all rows together
        return ''.join(rows)