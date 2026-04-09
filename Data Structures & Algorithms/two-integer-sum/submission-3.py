class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            complement = target - nums[i]

            if complement in mp:
                return [mp[complement], i]

            mp[n] = i