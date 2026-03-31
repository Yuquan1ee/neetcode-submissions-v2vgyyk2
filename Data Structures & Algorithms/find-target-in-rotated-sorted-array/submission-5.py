class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1
        while(start_index +1 < end_index):
            mid_index = (start_index + end_index)//2
            if target == nums[mid_index]:
                return mid_index

            if nums[start_index]<nums[mid_index]<nums[end_index]: #The list is inorder
                if target>nums[mid_index]:
                    start_index = mid_index
                else:
                    end_index = mid_index

            elif nums[mid_index]<nums[start_index] and nums[mid_index]<nums[end_index]:#start is at the left side of mid_index
                if nums[mid_index]<target<=nums[end_index]:
                    start_index = mid_index
                else:
                    end_index = mid_index
            elif nums[mid_index]>nums[start_index] and nums[mid_index]>nums[end_index]:
                if nums[start_index]<=target<nums[mid_index]:
                    end_index = mid_index
                else:
                    start_index = mid_index

        print(start_index,end_index)
        if nums[start_index] == target:
            return start_index
        elif nums[end_index] == target:
            return end_index
        else:
            return -1
                