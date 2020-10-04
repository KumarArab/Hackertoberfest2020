class Solution(object):
    def longestCommonPrefix(self, strs):
        if(len(strs) < 1):
            return("")
        prefs = strs[0]
        for i in strs:
            temp = ""
            for j in range(0, len(i)):

                if(j < len(prefs)):
                    if(prefs[j] == i[j]):
                        temp += i[j]
                    else:
                        break
            prefs = temp
        return (prefs)