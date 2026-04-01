class Solution(object):
    newNums = []
    def runningSum(self, nums):
        for i in nums:
            newNums.insert(i, nums[i] + i)
        return newNums