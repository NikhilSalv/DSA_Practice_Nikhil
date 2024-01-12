from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] = 1
            
            res[tuple(count)].append(s)
            # print(res) 
        return res
    

input = ["ate","ant","tan","eat","tea", "car", "rac"]

solution = Solution()

results = solution.groupAnagrams(input)
print(results)