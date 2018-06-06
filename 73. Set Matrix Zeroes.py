
# coding: utf-8

# In[ ]:


# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstrow=1
        firstcol=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstrow = 0
                    if j == 0:
                        firstcol = 0
                    if i !=0 and j !=0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if  matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j]=0
        if firstrow == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if firstcol == 0:
            for j in range(len(matrix)):
                matrix[j][0] = 0
                                
        

