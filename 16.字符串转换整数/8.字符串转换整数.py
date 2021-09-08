import re
class Solution:
    def myAtoi(self, s):
        """
        :param s:: str
        :return: -> int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # 清除左边多余的空格
        str = s.lstrip()
        # 设置正则规则
        num_re = re.compile(r'^[\+\-]?\d+')
        num = num_re.findall(str)
        num = int(*num)
        return max(min(num,INT_MAX),INT_MIN)

A = Solution()
print(A.myAtoi("   -42"))

