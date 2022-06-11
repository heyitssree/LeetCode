def int_reverse(x: int) -> int:
    reversed_int = 0
    while(x!=0):
        digit = x % 10
        reversed_int = reversed_int *10 + digit
        x = x // 10
    return(reversed_int)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            if(int_reverse(x)==x):
                return True
            else:
                return False