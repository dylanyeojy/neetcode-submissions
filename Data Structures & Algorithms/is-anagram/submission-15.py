class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = defaultdict(int)
        secondDict = defaultdict(int)

        for i in s:
            firstDict[i] += 1

        for i in t:
            secondDict[i] += 1
        
        return firstDict == secondDict