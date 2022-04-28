"""Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and
only the integer part of the result is returned.

NOTE: You are not allowed to use any built-in exponent function or operator,
    such as pow(x, 0.5) or x ** 0.5.

Constraints:
    0 <= x <= 231 - 1

TC: O(log(n))
SC: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = int(left + (right - left) / 2)
            if mid == x/mid:
                return mid
            if mid < x/mid:
                left = mid + 1
            else:
                right = mid - 1

        return right
