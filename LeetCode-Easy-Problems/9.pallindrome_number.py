class Solution(object):
    def isPalindrome(self, x):
        savednum = x
        if(x < 0):
            return False
        newnum = 0
        while(x != 0):
            rem = x%10
            newnum = newnum*10 + rem
            x //= 10
        if(newnum == savednum):
            return True
        else:
            return False