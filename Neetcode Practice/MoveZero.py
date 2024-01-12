"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        prev_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # hold = nums[prev_idx]
                nums[prev_idx], nums[i] = nums[i], nums[prev_idx]
                # nums[i] = hold
                prev_idx += 1
        return nums

nums = [0,1,0,0,3,12,3,2,1,0,2,32,13,0,1]

solution = Solution()

results = solution.moveZeroes(nums)

print(results)