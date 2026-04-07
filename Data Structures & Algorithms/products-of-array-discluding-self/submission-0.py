class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [0] * n
        for j in range(n):
            prod = 1
            for i in range(n):
                if i == j:
                    continue
                prod *= nums[i]
            result[j] = prod
        return result