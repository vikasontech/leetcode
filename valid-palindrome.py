# https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isSmallCase(s: str) -> bool:
            return ord(s) in range(97, 122+1)

        def convertToUpperCase(s) -> int:
            if isSmallCase(s):
                return ord(s) - 32
            else:
                return ord(s)

        def isLetter(s: str) -> bool:
            return (ord(s) in range(65, 90+1)
                    or ord(s) in range(97, 122+1)
                    or ord(s) in range(48,57+1))

        if(len(s.strip()) == 0):
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if not isLetter(s[l]):
                l += 1
                continue
            if not isLetter(s[r]):
                r -= 1
                continue
            if (convertToUpperCase(s[l]) != convertToUpperCase(s[r])):
                return False
            l += 1
            r -= 1

        return True


s = Solution()
assert not s.isPalindrome('radhe'), "1. incorrect"
assert  s.isPalindrome('A man, a plan, a canal: Panama'), "2. incorrect"
assert not s.isPalindrome('race a car'), "3. incorrect"
assert s.isPalindrome(' '), "4. incorrect"
assert not s.isPalindrome('0P'), "5. incorrect"
