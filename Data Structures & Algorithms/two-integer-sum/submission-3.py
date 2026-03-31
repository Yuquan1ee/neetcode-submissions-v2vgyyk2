class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i in range(0, len(nums)):
            if target - nums[i] in dict_num:
                return [dict_num[target - nums[i]], i]
            else:
                dict_num[nums[i]] = i


        return False