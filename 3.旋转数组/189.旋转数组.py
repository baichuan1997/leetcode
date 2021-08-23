class Solution:
    def rotate(self, nums, k):
        """
        :param nums: : List[int]
        :param k: : int
        :return:  -> None
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法1：三次反转
        # n = len(nums)
        # k %= n
        # def reverse(i,j):
        #     while i < j:
        #         nums[i] , nums[j] = nums[j], nums[i]
        #         i += 1
        #         j -= 1
        #
        # reverse(0, n-k-1)
        # reverse(n-k, n-1)
        # reverse(0, n-1)
        # return nums

        # 方法2：使用数组的反转
        n = len(nums)
        k = k%n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums


A = Solution()
print(A.rotate([1, 2, 3, 4, 5, 6, 7], 3))