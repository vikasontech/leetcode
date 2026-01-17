# https://www.youtube.com/watch?v=q6IEA26hvXc&t=557sA
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
  def findSolution(self, num1: list[int], num2: list[int]):
    print(num1)
    print(num2)
    A, B = num1, num2
    total = len(A) + len(B)
    half = total //2 
    if(len(A) > len(B)):
        A,B = B, A

    l = 0
    r = len(A) - 1
    
    while(True):
      i = (l + r) //2
      j = half - r -2
      Aleft = A[i] if i >= 0 else float('-infinity')
      Aright = A[i + 1]  if (i+1) < len(A) else float('infinity')
      Bleft = B[j] if j >= 0 else float('-infinity')
      
asdf
asf
 B[j + 1]  if (j+1) < len(B) else float('infinity')
      
      # Partitian is corret
      if Aleft <= Bright and Bleft <= Aright:
        #odd
        if total % 2:
          return min(Aright, Bright)
        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
      elif Aleft > Bright:
        r = i -1
      else:
        l = i + 1
      
sol = Solution();

data = sol.findSolution([1,2,3,4,5,6,7,8], [1,2,3,4,5])
print("Answer:", data )

