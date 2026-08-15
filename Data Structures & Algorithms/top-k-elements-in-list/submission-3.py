class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_list = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, cnt in count.items():
            count_list[cnt].append(num)

        res = []
        for i in range(len(count_list) - 1, 0 , -1):
            for num in count_list[i]:
                res.append(num)
                if len(res) == k:
                    return res

