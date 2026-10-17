class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_index = 0
        last_index = len(numbers) - 1

        lowest_num = numbers[first_index]
        highest_num = numbers[last_index]
        sum = lowest_num + highest_num

        while sum != target:
            if sum < target:
                first_index += 1
                lowest_num = numbers[first_index]
            else: # sum > target
                last_index -= 1
                highest_num = numbers[last_index]
            
            sum = lowest_num + highest_num

        if sum == target:
            return [first_index + 1, last_index + 1]
                