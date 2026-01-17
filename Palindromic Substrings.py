class Solutions:
    def countSubstrings(self, s: str) -> int:
        count = 0 
        for i in range(len(s)) :
            left,right = i, i
            while(left >=0 and right < len(s) and
                  s[left] == s[right]):
                left -= 1
                right += 1
                count+=1
        for i in range(len(s)) :
            left,right = i, i+1
            while(left >=0 and right < len(s) and
                  s[left] == s[right]):
                left -= 1
                right += 1
                count+=1
        return count

sol = Solutions()
print( "this is lendght: " , sol.countSubstrings("abcdd"))