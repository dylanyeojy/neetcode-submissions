class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: # to prevent using the same value twice for two sum
                continue
            
            # two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = num + nums[left] + nums[right]

                if threeSum == 0:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1

        return output

