class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        arr = []
        for key, value in d.items():
            arr.append([value, key]) # if did [key, value] would need to do arr.sort(key=lambda x:x[1]) to sort by value
        arr.sort()

        top_k = []
        while len(top_k) < k:
            top_k.append(arr.pop()[1]) 

        return top_k
        