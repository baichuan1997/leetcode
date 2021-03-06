# # 1.快慢指针法
# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :param nums:
#         :return:
#         """
#         if not nums:
#             return 0
#         n = len(nums)
#         fast = slow = 0
#         while fast < n:
#             if nums[fast] != nums[slow]:
#                 nums[slow+1] = nums[fast]
#                 slow += 1
#             fast += 1
#         return slow+1, nums[:slow+1]
#
# A = Solution()
# num, nums = A.removeDuplicates([1,1,1,2,2,2,3,3,4])
# print(num)
# print(nums)


# 2.暴力穷举法
class Solution:
    def removeDuplicates(self, nums):
        """
        :param nums:
        :return:
        """
        num = []
        for i in nums:
            if i not in num:
                num.append(i)
        return len(num)


A = Solution()
nums = A.removeDuplicates([1,1,2])

print(nums)