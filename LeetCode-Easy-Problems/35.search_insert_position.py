class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            #return index
            for i in range(0, len(nums)):
                if nums[i] == target:
                    return i
        else:
            nums.sort()
            for i in range(0,len(nums)):
                if nums[i] > target:
                    return i
            if target > nums[len(nums)-1]:
                return len(nums)
                