# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=oizxjoit
# two-pointer

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        length = len(prices)
        if length == 1:
            return 0

        bi, si, profit = 0,1,0
        bv, sv = prices[bi], prices[si]

        for i in range(length -1 ) :
            if (bv > prices[i]):
                bi = i
                bv = prices[bi]
            if sv < prices[i + 1] or si <= bi:
                si = i+1
                sv = prices[si]
            profit = max(sv-bv, profit)
        return max(profit,0)


s = Solution()
assert 5 == s.maxProfit([7,1,5,3,6,4]), '1'
assert 0 == s.maxProfit([7,6,4,3,1]), '2'
assert 4 == s.maxProfit([3,2,6,5,0,3]), '2'
assert 2 == s.maxProfit([2,1,2,1,0,1,2]), '2'
