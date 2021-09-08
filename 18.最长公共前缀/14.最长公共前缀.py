class Solution:
    def longestCommonPrefix(self, strs):
        """
        :param strs: : List[str]
        :return:  -> str
        """
        if not strs:
            return ""
        str0 = min(strs)
        str1 = max(strs)
        print(str0,str1)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

A = Solution()
# print(A.longestCommonPrefix(["flower","flow","flight"]))

# print(min(["flower", "flow", "flight"]))
strs = ["flower", "flow", "flight"]
print(zip(*strs))