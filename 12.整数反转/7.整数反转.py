class Solution:
    def reverse(self, x):
        """
        :param x: : int
        :return:  -> int
        """
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] == "-":
            x = -int(str_x[:0:-1])
        else:
            x =  int(str_x[::-1])
        return x if -2**31 < x < 2**31 else 0

A = Solution()
print(A.reverse(-321))

