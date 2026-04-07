class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # 1. HashSet 
        # 2. HashMap?


        hs = set(nums)

        if(len(hs) == len(nums)):
            return False
        
        else:
            return True

        ##print(hs)


        