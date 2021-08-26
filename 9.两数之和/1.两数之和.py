class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: : List[int]
        :param target: : int
        :return:  -> List[int]
        """
        map = dict()
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in map:
                return [map[temp], i]
            else:
                map[nums[i]] = i
