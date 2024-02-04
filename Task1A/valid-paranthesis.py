class Solution(object):
    def isValid(self, s):
        m = []
        for i in range(0, len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                m.append(s[i])
            else:
                if len(m) == 0:
                    return False 
                if s[i] == ')' and m[-1] == '(':
                    m.pop()
                elif s[i] == ']' and m[-1] == '[':
                    m.pop()
                elif s[i] == '}' and m[-1] == '{':
                    m.pop()
                else:
                    return False 
        if len(m) > 0:
            return False
        else: 
            return True