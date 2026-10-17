class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for character in s:
            if not (character in dict_s):
                dict_s.update({character: 1})
            else:
                curr_value = dict_s[character]
                dict_s.update({character: curr_value + 1})

        for character in t:
            if not (character in dict_t):
                dict_t.update({character: 1})
            else:
                curr_value = dict_t[character]
                dict_t.update({character: curr_value + 1})
        
        if dict_s == dict_t:
            return True
        else:
            return False