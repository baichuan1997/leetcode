class Solution:
    def containsDuplicate(self, nums):
        """
        :param nums: : List[int]
        :return:  -> bool
        """
        # 方法1：使用set函数
        # return len(list(set(nums))) != len(nums)

        # 方法2：遍历
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
A = Solution()
print(A.containsDuplicate([1, 2, 1]))

