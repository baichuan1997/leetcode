class Solution:
    def reverseString(self, s):
        """
        :param s: : List[str]
        :return:  -> None
        """
        """
        Do not return anything, modify s in-place instead.
        """
        # 第一种方法
        # s[:] = s[::-1]

        # 第二种方法
        left = 0
        right = len(s)-1
        while left<right:
            s[right], s[left] = s[left], s[right]
            left +=1
            right -=1

        return s

A = Solution()
print(A.reverseString(["h", "e", "l", "l", "o"]))
