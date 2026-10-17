class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {} # store difference: value

        for i in range(len(nums)):
            difference = target - nums[i]
            
            if not difference in diff_dict:
                diff_dict.update({nums[i]: i})
            else:
                value = diff_dict.get(difference)
                return [value, i]
