class Solution:
    def intersect(self, nums1, nums2):
        """
        :param nums1: : List[int]
        :param nums2: : List[int]
        :return:  -> List[int]
        """
        nums1.sort()
        nums2.sort()
        len1, len2 = len(nums1), len(nums2)
        num = []
        index1, index2 = 0, 0
        while index1<len1 and index2<len2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                num.append(nums1[index1])
                index1 +=1
                index2 +=1
        return num

A = Solution()
print(A.intersect([1, 2, 2, 1], [2, 2]))