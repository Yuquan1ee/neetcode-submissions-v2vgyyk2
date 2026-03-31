class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i in range(0, len(nums)-2):
            
            left = i+1
            right = len(nums) - 1
            target = 0 - nums[i]
            while(left<right):
                if nums[left] + nums[right] == target:
                    answer.add((nums[i], nums[left], nums[right]))
                    left = left +1 
                    right = right -1
                elif  nums[left] + nums[right] > target:
                    right = right - 1
                elif nums[left] + nums[right] < target:
                    left = left + 1
        print(answer)

        return list(answer)



    #This is optimal. Do not use a hash map 