class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 暴力解法
        # max_profit = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         max_profit = max(max_profit, prices[j] - prices[i])
        #         print(max_profit)
        # return max_profit

        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit


A = Solution()
print(A.maxProfit([7, 1, 5, 3, 6, 4]))