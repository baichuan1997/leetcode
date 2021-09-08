class Solution:
    def strStr(self, haystack, needle):
        """
        :param haystack:: str
        :param needle:: str
        :return:  -> int
        """
        if len(needle)==0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i:len(needle)+i] == needle:
                    return i

A = Solution()
print(A.strStr("aaaaa", "bba"))



