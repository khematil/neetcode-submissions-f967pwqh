class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0 
        right = len(nums) - 1
        # Case 1: nums[left] < nums[right]
        if nums[left] < nums[right]:
            return nums[left]

        else:
        # Case 2: nums[left] >= nums[right]

            while left < right: 
                mid = left + (right - left) // 2

                if nums[mid] <= nums[-1]:
                    right = mid 
                
                else: 
                    left = mid + 1

            return nums[left]
        