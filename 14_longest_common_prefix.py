"""Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

TC: O(n*m); m - shortest string length
SC: O(1)
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(item) for item in strs])

        if min_length == 0:
            return ''

        for index in range(min_length):
            c = strs[0][index]
            for item in strs[1:]:
                if item[index] != c:
                    return strs[0][:index]

        return strs[0][:min_length]
