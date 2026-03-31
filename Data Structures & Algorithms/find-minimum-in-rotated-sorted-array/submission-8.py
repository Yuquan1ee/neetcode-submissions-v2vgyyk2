class Solution:
    def findMin(self, nums: List[int]) -> int:
        start_index = 0
        end_index = len(nums) - 1
        while(start_index + 1< end_index):
            mid_index = (start_index+end_index)//2
            if nums[mid_index]>nums[start_index] and nums[mid_index]>nums[end_index]:
                start_index = mid_index
            elif nums[mid_index]<nums[start_index] and nums[mid_index]<nums[end_index]:
                end_index = mid_index
            else:
                return nums[start_index]
        print(start_index, end_index)

        if nums[end_index]>nums[start_index]:
            return nums[start_index]
        else:
            return nums[end_index]
