class Solution(object):
    def strStr(self, haystack, needle):
        if((haystack == "" and needle == "") or (haystack != "" and needle == "")):
            return 0
        if(needle in haystack):
            needle_length = len(needle)
            count = 0
            start = -1
            i = 0
            while i in range(0, len(haystack)):
                if(count < needle_length):
                    if (haystack[i] == needle[count]):
                        if(start == -1):
                            start = i
                        count += 1
                    elif(haystack[i] != needle[count] and count != 0):
                        i = start
                        start = -1
                        count = 0
                    i += 1
                        
                else:
                    return start
            return start
        else:
            return -1