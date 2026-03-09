class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_s = ''
        l, r = 0, 0

        while r < len(s):
            if (s[r] == ' '):
                reversed_s += s[l:r][::-1] + ' '
                l = r+1
                
            r += 1

        reversed_s += s[l:r][::-1]
        return reversed_s