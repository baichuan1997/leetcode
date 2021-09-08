class Solution:
    def isPalindrome(self, s):
        """
        :param s:: str
        :return: -> bool
        """
        ret = []
        for i in s:
            if i.isalnum():
                ret.append(i.lower())
        return ret==ret[::-1]

A = Solution()
print(A.isPalindrome("A man, a plan, a canal: Panama"))