class Solution(object):
    def reverse(self, x):
        if(x < 2147483647 and x > -2147483648):
            flag = False
            if(x < 0):
                flag =True
                x = -x
            newnum = 0
            while(x != 0):
                rem = x%10
                newnum = newnum*10 + rem
                x //= 10
            if(newnum < 2147483647 and newnum > -2147483648):
                if(flag):
                    return(newnum*-1)
                else:
                    return(newnum)
            else:
                return("0")
        else:
            return("0")
        