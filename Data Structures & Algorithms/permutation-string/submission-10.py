class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # optimal solution not O(26 * n) but just O(n)

        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        matches = 0
        left = 0

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

            
        for right in range(len(s1), len(s2)):

            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')


            s2_count[index] += 1

            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] + 1:
                matches-=1

            
            while (right - left + 1) > len(s1):
                index = ord(s2[left]) - ord('a')
                s2_count[index] -= 1

                if s1_count[index] == s2_count[index]:
                    matches += 1
                elif s2_count[index] == s1_count[index] - 1:
                    matches-=1

                left+=1


        return matches == 26

