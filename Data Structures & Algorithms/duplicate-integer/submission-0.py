class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkedNums = []
        for num in nums:
            if num in checkedNums:
                return True
            else:
               checkedNums.append(num)
        
        return False


            
     