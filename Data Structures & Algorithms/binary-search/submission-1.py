class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid 
            
            elif nums[left] < target:
                left+=1

            else:
                right-=1


        return -1



        
        