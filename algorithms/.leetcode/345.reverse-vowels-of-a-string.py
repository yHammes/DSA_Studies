
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        string = list(s)

        l = 0
        r = len(string) - 1

        while l < r:
            while l < r and vowels.find(string[l]) == -1:
                l += 1
                
            while l < r and vowels.find(string[r]) == -1:
                r -= 1

            string[l], string[r] = string[r], string[l]

            l += 1
            r -= 1

           

        return "".join(string)
    
print(Solution().reverseVowels("String Reversed"))