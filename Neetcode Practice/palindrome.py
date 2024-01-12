class Solution(object):
    def isPalindrome(self,s):
        s = s.replace(" ", "").replace(",","").repl.lower()
        return s


s = "A man, a plan, a canal: Panama"

solution = Solution()
results = solution.isPalindrome(s)
print(results)