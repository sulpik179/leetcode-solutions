class Solution:
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            for num in range(index + 1, len(nums)):
                if nums[index] + nums[num] == target:
                    return index, num

        


