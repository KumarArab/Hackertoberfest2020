class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        if(n >= 1 and n <= 30):
            num = 1
            cands = "1"
            while(num < n):
                count = 0
                act = 0
                temp = ""
                for i in cands:
                    if i != act:
                        if count != 0:
                            temp += str(count)
                            temp += str(act)
                        count = 1
                        act = i
                    else:
                        count += 1
                temp += str(count)
                temp += str(act)
                cands = temp
                num += 1
            return cands