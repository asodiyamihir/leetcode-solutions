# Title: Reverse Integer
# Submission ID: 2133167546
# Status: Accepted
# Date: September 6, 2026 at 11:36:49 PM GMT+5:30

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2**31          # -2147483648
        INT_MAX = 2**31 - 1       #  2147483647

        rev = 0
        sign = 1

        # Handle negative numbers
        if x < 0:
            sign = -1
            x = -x

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before adding the digit
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            rev = rev * 10 + digit

        return sign * rev