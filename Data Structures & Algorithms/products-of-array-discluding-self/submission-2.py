class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_side = [1]
        left_side = [1]
        right_value = 1
        left_value = 1
        for i in range(0, len(nums)-1):
            left_value = left_value * nums[i]
            left_side.append(left_value)
            right_value = right_value * nums[len(nums)-i-1]
            right_side.insert(0,right_value)
        
        for i in range(0,len(left_side)):
            left_side[i] = left_side[i] * right_side[i]
        return left_side