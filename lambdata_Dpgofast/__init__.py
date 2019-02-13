'''lambdata- A Data Science Helper
'''
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

ONES = np.ones(100)
ONES_DF = pd.DataFrame(ONES)

class DataSci:
    '''Creates useful functions for use in DataScience'''
    def sqrt(n):
      return n ** 0.5

    def mean(nums):
        return sum(nums) / len(nums)

    def variance(nums, sample=False):
        if sample:
             return sum((x - mean(nums)) ** 2 for x in nums) / (len(nums) - 1)
        else:
            return sum((x - mean(nums)) ** 2 for x in nums) / len(nums)

    def stdev(nums):
        return sqrt(variance(nums))
  
    def zscore(n, nums):
        return (n - mean(nums)) / stdev(nums)
  
    def find_outliers(nums, threshold=1):
        outliers = []
        for i in range(len(nums)):
            if abs(zscore(nums[i],nums)) > threshold:
                outliers.append(nums[i])
        return outliers
