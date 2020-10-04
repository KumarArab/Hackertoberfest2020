class Solution:
    def twoSum(self, nums, target):
        temp = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    temp.append(i)
                    temp.append(j)
        return temp
