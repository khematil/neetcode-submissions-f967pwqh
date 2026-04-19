from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:


        if key not in self.timeMap:
            return ""
        

        values = self.timeMap[key]
        left = 0 
        right = len(values)

        while left < right: 
            mid = left + (right - left) // 2

            if values[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        if left-1 < len(values) and values[left-1][0] <= timestamp:
            return values[left-1][1]

        return ""
        
