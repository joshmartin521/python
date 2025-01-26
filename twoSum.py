class Solution(object):
    def twoSum(self, nums, target):
        myHash = {}
        for i in range(len(nums)):
            if target - nums[i] in myHash:
                return [myHash[target - nums[i]], i]
            myHash[nums[i]] = i
