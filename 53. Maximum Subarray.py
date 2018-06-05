
# coding: utf-8

# In[12]:


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxtemp = nums[0]
        sumtemp = 0
        for i in range(len(nums)):
            if sumtemp>=0:
                sumtemp+=nums[i]
            else:
                sumtemp=nums[i]
            
            if sumtemp>maxtemp:
                maxtemp = sumtemp
        return maxtemp
                    
                

