

class Solution(object):
    def longestConsecutive(self, nums):

        numSet = set(nums)
        longest  = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length = length + 1 
                longest = max(longest,length)
        return longest
    

nums = [0,3,7,2,5,8,6,0,1]
solution = Solution()
results = solution.longestConsecutive(nums)
print(results)