#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

from re import split
# @lc code=start


class Solution:
    def reverseWords(self, s: str) -> str:
        words = split(" ", s)
        words_inverted = []

        for i in range(len(words)):
            word = words[len(words) - i - 1]

            if not word.strip() == "":
                words_inverted.append(word)

        return " ".join(words_inverted).strip()
# @lc code=end

print(Solution().reverseWords("the sky is blue"))
