import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        s = s.translate(str.maketrans('', '', string.punctuation))
        
        reversed_s = list(s)
        reversed_s.reverse()
        reversed_s = ''.join(reversed_s)

        return s == reversed_s
            
        # print(s)
        # print(reversed_s)

        