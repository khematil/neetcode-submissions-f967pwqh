class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        left = 0
        res = [-1, -1]
        resLen = float("inf")
    
        countT = {}
        sWindow = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0 
        need = len(countT)


        for right in range(len(s)):
            c = s[right]
            sWindow[c] = sWindow.get(c, 0) + 1

            if c in countT and sWindow[c] == countT[c]:
                have += 1


            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)

                sWindow[s[left]] -= 1


                if s[left] in countT and sWindow[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1


            print(res)

        left, right = res


        if resLen != float('inf'):
            return s[left: right + 1]
            
        
        return ""