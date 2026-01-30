# https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def isValidParenthesis(self, s: str) -> bool:
        return True

    def longestValidParentheses2(self, s: str) -> int:
        # Initialize stack with -1 to handle the base case for the first valid pair
        stack = [-1]
        mx = 0
        open, close = '(',')'
        for i, char in enumerate(s):
            if char == open:
                # Push the index of the opening bracket
                stack.append(i)
            else:
                # It's a ')', pop the last opening bracket or boundary
                stack.pop()

                if not stack:
                    # If stack is empty, this ')' is a new boundary
                    stack.append(i)
                else:
                    # Calculate length: current index - index of the last unmatched bracket
                    mx = max(mx, i - stack[-1])
        return mx

s = Solution()
# print(s.longestValidParentheses2(")()()())()"))
# assert s.longestValidParentheses2(")()()())()")==6, "1. wrong answer"
# assert s.longestValidParentheses2("(()")==2, "2. wrong answer"
# assert s.longestValidParentheses2(")()())")==4, "3. wrong answer"
# assert s.longestValidParentheses2("")==0, "4. wrong answer"
# assert s.longestValidParentheses2("))")==0, "5. wrong answer"
# assert s.longestValidParentheses2(")")==0, "6. wrong answer"
# assert s.longestValidParentheses2("))())")==2, "7. wrong answer"
# assert s.longestValidParentheses2("(((")==0, "8. wrong answer"
# assert s.longestValidParentheses2("()(())")==6, "9. wrong answer" # fail
assert s.longestValidParentheses2("()(()")==2, "9. wrong answer" # fail
