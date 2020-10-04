class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return nums[0]
        else:
            max_sum = nums[0]
            current_sum = nums[0]
            for i in range(1,len(nums)):
                current_sum = max(current_sum+nums[i],nums[i])
                max_sum = max(max_sum,current_sum)
            return max_sum