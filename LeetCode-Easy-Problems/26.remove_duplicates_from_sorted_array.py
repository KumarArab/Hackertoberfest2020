class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        i = 0
        while(i < len(nums)-1):
            if(nums[i+1] == nums[i]):
                nums.remove(nums[i+1])
            else:
                i += 1
        print(nums)
        return len(nums)