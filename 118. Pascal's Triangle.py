
# coding: utf-8

# In[17]:


# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(numRows):
            innerresult = []
            for j in range(i+1):
                if j == 0 or j == i:
                    innerresult.append(1)
                else:
                    innerresult.append(result[i-1][j-1]+result[i-1][j])
            result.append(innerresult)
        
        return result

