# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=xi4ci4ig
class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(',
               ']':'[',
               '}':'{',
               }
        stack = []

        for ch in s:
            # is closing bracket found?
            if ch in map:
                # if the first char is clocking bracket
                if len(stack) == 0:
                    return False

                comb = stack.pop()
                if map.get(ch) != comb:
                    return False
            else:
                stack.append(ch)

        return True and len(stack) == 0


s = Solution()
assert s.isValid("()") , "1. assertion failed"
assert s.isValid("()[]{}") , "2. assertion failed"
assert not s.isValid("(]") , "3. assertion failed"
assert s.isValid("([])") , "4. assertion failed"
assert not s.isValid("([)]") , "5. assertion failed"
assert not s.isValid("[") , "5. assertion failed"
assert not s.isValid("]") , "5. assertion failed"
assert not s.isValid("]]") , "5. assertion failed"