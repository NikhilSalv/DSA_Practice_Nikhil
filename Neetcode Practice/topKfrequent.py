"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

class Solution(object):
    def topKFrequent(self,nums,k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        occasions = {}
        for integer in nums:
            occasions[integer] = occasions.get(integer,0) + 1

        sorted_occasions = dict(sorted(occasions.items(), key= lambda x : x[1],reverse=True ))

        return list(sorted_occasions.keys())[:k]




nums = [1,1,1,1,2,2,3,3,3,3,3,4,4,2,3,3,1,2,1,2,5]

solution = Solution()
occ_results = solution.topKFrequent(nums,3)

print(occ_results)

freq = [[] for i in range(len(nums) + 1 )]


freq[3].append(33)
print(freq)

# my_dict = {10: 3, 30:4, 45: 22, 50 : 1 , 65: 0, 7: 0}

# print(my_dict.items())

# def sorted_dict_fun(a):
#     return a[1]

# results = sorted_dict_fun(my_dict)

# print(results)