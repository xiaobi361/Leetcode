
# coding: utf-8

# In[ ]:


# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in nums:
            for j in result[:]: #here result[:] not result; use result->bug: Time Limit Exceeded
                x = j[:]
                x.append(i)
                result.append(x)
        return result
    
# #result[:],分片,如果不带分片，就是一个浅拷贝，后面result有变化，导致result不断增加，for一直进行下去
# 分片操作用来访问一定范围内的元素，通过在方括号内用冒号隔开两个索引来实现。第一个索引的元素是开始点，包括在结果之中，第二个索引的元素是结束点，不包括在结果之中
# 注意：分片中最左边的索引要比它右边索引出现的早，否则就会成为空列表。
# >>> num=[1,2,3,4,5,6,7,8,9,10] 
# 捷径1：访问倒数几个元素（包括最后一个元素）。
# [python] view plain copy
# >>> num[-3:]  
# [8, 9, 10]  
# >>>  

# 捷径2：访问前面几个元素（包括第一个元素）。
# [python] view plain copy
# >>> num[:4]  
# [1, 2, 3, 4]  
# >>>  

# 捷径3：访问全部元素。
# [python] view plain copy
# >>> num[:]  
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# >>> 
# 其实，分片除了开始点和结束点外还有一个参数，就是步长。通常步长都是隐式设置的，像以上所有例子中步长都是隐式设置为1了。步长可以为正数，可以为负数，但不能为0.

# [python] view plain copy
# >>> num[10:0:2]  
# []  
# >>> num[::1]  
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# >>> num[::2]  
# [1, 3, 5, 7, 9]  
# >>> num[3:7:3]  
# [4, 7]  
# >>>  

