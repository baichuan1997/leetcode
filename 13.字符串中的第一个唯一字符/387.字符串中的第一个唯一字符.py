# class Solution:
#     def firstUniqChar(self, s):
#         """
#         :param s: : str
#         :return: -> int
#         """
#         s = list(str(s))
#         slow = 0
#         fast = 1
#         while slow<len(s)-1:
#             if s[slow] != s[fast]:
#                 fast +=1
#                 if fast == len(s):
#                     return slow
#             else:
#                 slow+=1
#         return -1

class Solution:
    def firstUniqChar(self, s):
        d = {}
        length = len(s)
        for i in range(length):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = length + 1
        ret = min(d.values())
        return -1 if ret > length else ret


A = Solution()
print(A.firstUniqChar("looheleetcode"))
