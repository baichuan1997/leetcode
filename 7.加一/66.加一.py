class Solution:
    def plusOne(self, digits):
        """
        :param digits: : List[int]
        :return:  -> List[int]
        """
        num = int(''.join([str(s) for s in digits])) + 1
        return [int(s) for s in str(num)]





