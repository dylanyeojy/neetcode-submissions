import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)
        cleaned_s = s.translate(translator).lower().replace(" ", "")

        reversed_s = list(cleaned_s)
        reversed_s.reverse()
        reversed_s = ''.join(reversed_s)

        return reversed_s == cleaned_s