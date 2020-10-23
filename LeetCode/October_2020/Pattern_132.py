'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

    Input: nums = [1,2,3,4]
    Output: false
    Explanation: There is no 132 pattern in the sequence.
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        for i in range(len(nums)-2):
            big = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:                    
                    if nums[j] < big:
                        return True
                    elif nums[j] > big:
                        big = nums[j]       
						
        return False