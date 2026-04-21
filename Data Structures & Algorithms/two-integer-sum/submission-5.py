class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        n = len(nums)

        for i, val in enumerate(nums):
            complement = target - val

            if complement in mp:
                return [mp[complement], i]

            mp[val] = i