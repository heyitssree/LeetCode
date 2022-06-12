def rev_string(s: str) -> str:
    rev = ""
    for i in s:
        rev = i + rev
    return rev
def formatting(s: str) -> str:
    s = re.sub("[^0-9a-zA-Z]+", "", s)
    s = s.lower()
    return s

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = formatting(s)
        rev = rev_string(s)
        print(s)
        print(rev)
        if (s==rev):
            return True
        else:
            return False