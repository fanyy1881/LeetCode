'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data_dict = {}
        for i, value in enumerate(nums):
            if (target - value) in data_dict:
                return [data_dict[target - value], i]
            data_dict[value] = i

if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum([3, 3, 4], 6))