class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_dict = {}
        for i in range(0, len(nums)):
            for x in range(i+1, len(nums)):
                total = nums[i] + nums[x]
                if total not in sum_dict:
                    sum_dict[total] = []
                sum_dict[total].append([i,x])
        
        answer = set()
        for i in range(0, len(nums)):
            expect_sum = 0 - nums[i]
            if expect_sum in sum_dict:
                for x in sum_dict[expect_sum]:
                    first_value = x[0]
                    second_value = x[1]
                    if (i < first_value):
                        # Create a sorted tuple so it is hashable and avoids duplicates
                        triplet = tuple(sorted([nums[i], nums[first_value], nums[second_value]]))
                        answer.add(triplet)
                    
        return [list(t) for t in answer]