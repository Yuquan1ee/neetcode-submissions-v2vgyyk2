class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums)-1
        mid_index = (start_index + end_index)//2
        while(start_index+1 < end_index):
            mid_index = (start_index + end_index)//2
            if nums[mid_index] > target:
                end_index = mid_index
            elif nums[mid_index] < target:
                start_index = mid_index
            elif nums[mid_index] == target:
                return mid_index
            mid_index = (start_index + end_index)//2
        
        if nums[start_index] == target:
            return start_index
        elif nums[end_index] == target:
            return end_index
        else:
            return -1