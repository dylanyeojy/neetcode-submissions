class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = defaultdict(int)
        output = maxCount = 0

        for num in nums:
            numDict[num] += 1

            if maxCount < numDict[num]:
                output = num
                maxCount = numDict[num]

        return output