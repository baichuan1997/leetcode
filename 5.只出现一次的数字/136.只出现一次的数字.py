class Solution:
    def singleNumber(self, nums):
        """
        :param nums: : List[int]
        :return:  -> int
        """
        res = 0
        for i in nums:
            res = res ^ i
        return res
A = Solution()
print(A.singleNumber([1, 2, 1, 3, 3]))

