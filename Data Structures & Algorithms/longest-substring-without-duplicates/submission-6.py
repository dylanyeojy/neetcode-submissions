class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        greatestLen = 0
        charSet = set()
        left = 0

        for right in range(len(s)):
            while s[right] in charSet: # to remove duplicates, and to shrink the sliding window 
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            greatestLen = max(greatestLen, len(charSet))
        
        return greatestLen