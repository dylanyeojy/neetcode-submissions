class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for character in s:
            dict_s[character] = dict_s.get(character, 0) + 1

        for character in t:
            dict_t[character] = dict_t.get(character, 0) + 1
        
        return dict_s == dict_t
            