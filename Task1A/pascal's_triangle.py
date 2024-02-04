class Solution(object):
    def generate(self, numRows):
        a = [[1]]
        for i in range(1,numRows):
            a.append([0]*(i+1))
            a[i][0], a[i][-1] = 1, 1; 
            for j in range(1,i):
                a[i][j] = a[i-1][j] + a[i-1][j-1]
        return a