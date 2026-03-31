class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print(nums_set)
        max_consec = 0
        while(len(nums_set) != 0):
            current_consec = 1
            current = nums_set.pop()
            reduce = 1
            increase = 1
            while(current+increase in nums_set or current - reduce in nums_set):
                if current+increase in nums_set:
                    current_consec = current_consec + 1
                    nums_set.remove(current+increase)
                    increase = increase + 1
                if current - reduce in nums_set:
                    current_consec = current_consec + 1
                    nums_set.remove(current-reduce)
                    reduce = reduce + 1
            if current_consec > max_consec:
                max_consec = current_consec
        return max_consec
        
