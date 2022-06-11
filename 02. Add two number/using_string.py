def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(reverse(str(x))==str(x)):
            return True
        else:
            return False