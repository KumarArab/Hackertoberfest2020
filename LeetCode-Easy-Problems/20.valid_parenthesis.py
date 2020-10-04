class Solution(object):
    def isValid(self, s):
        if(len(s)%2 != 0):
            return False
        stack = []
        for i in s:
            if (i == "(" or i == "{" or i == "["):
                stack.append(i)
            elif (i == ")" and len(stack) != 0 and stack[-1] == "("):
                stack.pop()
            elif (i == "}" and len(stack) != 0 and stack[-1] == "{"):
                stack.pop()
            elif (i == "]" and len(stack) != 0 and stack[-1] == "["):
                stack.pop()
            else:
                return False
            
        if(len(stack) > 0):
            return False
        else: 
            return True