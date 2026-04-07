class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashset = set(nums)

        longest = 0


        for num in nums_hashset:
            if (num - 1) not in nums_hashset:
                length = 1
                while (num + length) in nums_hashset:
                    length+=1
                
                longest = max(length, longest)
            
        
        return longest
        