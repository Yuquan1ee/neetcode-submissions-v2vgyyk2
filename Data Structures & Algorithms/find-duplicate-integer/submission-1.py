class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums: # a total of n+1 digits in nums {index from 0 to n}
        
            if i < 0:
                i = i * -1
            
            if nums[i] < 0:
                return i
            else:
                nums[i] = nums[i] * -1

