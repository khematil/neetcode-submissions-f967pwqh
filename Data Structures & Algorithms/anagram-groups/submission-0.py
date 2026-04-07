class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringMap = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in stringMap:
                stringMap[sortedS] = []
            stringMap[sortedS].append(s)

        return list(stringMap.values())