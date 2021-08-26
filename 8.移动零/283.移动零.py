class Solution:
    def moveZeroes(self, nums):
        """
        :param nums:  List[int]
        :return: ->None
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums


A = Solution()
print(A.moveZeroes([1, 0, 0, 3, 12]))

