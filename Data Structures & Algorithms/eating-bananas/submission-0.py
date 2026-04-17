class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right: 
            total_hrs = 0
            mid = left + (right - left) // 2

            for pile in piles:
                hrs_ceil = -((-pile) // mid)
                total_hrs+=hrs_ceil
            
            if total_hrs <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1


        return res