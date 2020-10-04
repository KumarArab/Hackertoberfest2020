class Solution(object):
    def plusOne(self, digits):
        s = [str(i) for i in digits] 
        strint = "".join(s)
        strint = int(strint)+1
        return [int(i) for i in str(strint)]
