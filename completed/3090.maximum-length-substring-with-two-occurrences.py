#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        chars = {}
        max_length = 0
        counter = 0
        l_pointer = 0
        r_pointer = 0

        while r_pointer < len(s):
            r_char = s[r_pointer]
            chars[r_char] = chars[r_char] + 1 if chars.get(r_char) else 1
            if (chars[r_char] == 3):
                max_length = counter if max_length < counter else max_length
                counter = 0
                while chars[r_char] == 3:
                    l_char = s[l_pointer]
                    chars[l_char] = chars[l_char] - 1
                    l_pointer += 1
                r_pointer = l_pointer
                chars = {}

            else:
                counter += 1
                r_pointer += 1

        max_length = counter if max_length < counter else max_length

        return max_length

   
print(Solution().maximumLengthSubstring("bcbbbcba"))
# @lc code=end

