class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        while(True):
            if target - numbers[left_pointer]- numbers[right_pointer] == 0:
                return [left_pointer + 1, right_pointer + 1]
            elif target - numbers[left_pointer] - numbers[right_pointer] > 0:
                left_pointer = left_pointer + 1
            else:
                right_pointer = right_pointer - 1
