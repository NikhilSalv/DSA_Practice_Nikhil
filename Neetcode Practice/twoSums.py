class Solution(object):

    def binarySearch(self, nos, startIndex, endIndex, target):
        if(startIndex > endIndex):
            return -1

        midIndex = startIndex + (endIndex - startIndex)//2
        if(target == nos[midIndex]):
            return midIndex
        
        if(target > nos[midIndex]):
            startIndex = midIndex + 1
        else:
            endIndex = midIndex - 1

        return self.binarySearch(nos, startIndex, endIndex, target)

    def twoSum(self, nums, target):
        length = len(nums)
        for index, number in enumerate(nums):
            pairNumber = target - number
            pairIndex = self.binarySearch(nums, 0, length - 1, pairNumber)
            # return [index, pairIndex]
            if(pairIndex != -1 and pairIndex != index):
                return [index, pairIndex]

# class Solution(object):
#     def twoSum(self, nums,target):
#         j = len(nums) - 1

#         for i in range(len(nums)):
#             while j > i:
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#                 elif nums[i] + nums[j] > target:
#                     j -= 1
#                 else:
#                     break
            

nums1 = [2,7,11,15]
nums2 = [1,3,4,5,6,7,9]
nums3 = [3,2,4]
target = 9

solution = Solution()

pair_results = solution.twoSum(nums1,target)
print(pair_results)