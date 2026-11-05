import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = s.translate(translator).replace(" ", "")
        length = len(cleaned_text)
        left = 0
        right = length - 1

        print(cleaned_text)

        while left < right:
            if cleaned_text[left].lower() != cleaned_text[right].lower():
                return False
            left += 1
            right -= 1

        return True