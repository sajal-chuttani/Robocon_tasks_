class Solution(object):
    def constructRectangle(self, area):
        f = []
        root = area ** 0.5
        root = int(root - (root%1))
        for i in range(1,root+1):
            if area % i == 0 :
                f.append([area/i,i])
        return f[-1]
        
