class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenVals = {}
        index = 0
        for i in nums:
            if (target - i) in seenVals:
                return sorted([index, seenVals[target - i]])
            seenVals[i] = index
            index += 1
