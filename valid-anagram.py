# https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=oizxjoit
from collections import defaultdict

class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        #followup Unicode:
        if len(s) != len(t):
            return False

        freq = defaultdict(int)

        for char in s:
            freq[char] += 1

        for char in t:
            freq[char] -= 1
            if freq[char] < 0:
                return False

        return True
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = dict()
        for i in range(len(s)):
            chs = s[i]
            cht = t[i]

            if (chs == cht):
                continue

            if (chs in map):
                chs_ = map[chs] + 1
                if(chs_ == 0):
                    map.pop(chs)
                else:
                    map[chs] = chs_
            else:
                map[chs] = 1

            if (cht in map):
                cht_ = map[cht] - 1
                if(cht_ == 0):
                    map.pop(cht)
                else:
                    map[cht] = cht_
            else:
                map[cht] = -1

        return len(map)==0


s = Solution()
print(s.isAnagram2("aa", "bb"))
print(s.isAnagram2("anagram", "nagaram"))
print(s.isAnagram2("rat", "car"))
print(s.isAnagram2("dgncpmbgmg", "dgggsmmtnc"))
