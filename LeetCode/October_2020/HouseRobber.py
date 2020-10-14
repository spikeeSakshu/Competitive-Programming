class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<4:return max(nums)
        l1=[nums[0],nums[1],nums[0]+nums[2]]
        l2=[0,nums[1],nums[2]]
        for i in range(3,len(nums)):
            l1.append(max(nums[i]+l1.pop(0),nums[i]+l1[0]))
            l2.append(max(nums[i]+l2.pop(0),nums[i]+l2[0]))
        return max(l1[0],l1[1],l2[2])