class Solution(object):
    def lengthOfLastWord(self, s):
        if len(s) == 0:
            return 0
        else:
            s = s.strip()
            word_arr = s.split(" ")
            return len(word_arr[-1])