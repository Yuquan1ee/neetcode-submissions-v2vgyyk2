class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       


# amend nums in place 



# Floyd's cycle detection can be used to prevent amendment in place

        slow = nums[0]
        fast = nums[0]

        # find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
