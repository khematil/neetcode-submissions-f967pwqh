class Solution:

    def encode(self, strs: List[str]) -> str:
        combinedString = ""

        if not strs:
            return combinedString
        
        for s in strs:
            sLength = len(s)
            combinedString += str(sLength) + "#" + s

        return combinedString



    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        i = 0 
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j+=1
                
            length = int(s[i:j]) 
            
            i = j + 1  
            j = i + length 
            
            result.append(s[i:j]) 
            
            i=j

        return result