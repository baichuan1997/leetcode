class Solution:
    def isAnagram(self, s, t):
        """
        :param s:: str
        :param t: : str
        :return:  -> bool
        """
        return sorted(s) == sorted(t)

A = Solution()
print(A.isAnagram("anagram", "nagaram"))

