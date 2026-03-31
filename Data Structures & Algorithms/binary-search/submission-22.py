class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) -1
        while(start_index<=end_index):
            mid_index = (start_index+end_index)//2 #2,3,4
            print(start_index,mid_index,end_index)
            if nums[mid_index]== target:
                return mid_index
            elif nums[mid_index]>target:
                end_index = mid_index-1
            elif nums[mid_index]<target:
                start_index = mid_index+1
            print(start_index,mid_index,end_index)
        return -1