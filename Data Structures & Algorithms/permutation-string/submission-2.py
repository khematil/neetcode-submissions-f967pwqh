class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        s1Map = {}
        s2Map = {}

        for char in s1: 
            s1Map[char] = s1Map.get(char, 0) + 1
        
        for right in range(len(s2)):
            s2Map[s2[right]] = s2Map.get(s2[right], 0) + 1

            # condition if window size > length of s1 we increase left pointer
            while (right - left + 1) > len(s1):
                s2Map[s2[left]] -= 1

                if s2Map[s2[left]] == 0:
                    del s2Map[s2[left]]

                left += 1
            
            print(s1Map)
            print(s2Map)
            if s1Map == s2Map:
                return True

        return False


