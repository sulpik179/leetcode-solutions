class Solution:
    def isPalindrome(self, x):
        l1 = list(str(x))
        l2 = list(str(x))
        l2.reverse()
        if l1 == l2:
            return True
        else:
            return False
