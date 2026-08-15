class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Pretty sure that this question is solved with a bucket type of system
        n = len(nums)
        nums = sorted(nums)
        freq = [[] for _ in range(n + 1)]
        counter = 0
        prev = nums[0]
        for i in range(len(nums)):
            candidate = nums[i]
            if prev == candidate:
                counter += 1
            else:
                freq[counter].append(prev)
                prev = candidate
                counter = 1
        freq[counter].append(prev)
        
        ret = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] != []:
                ret = ret + freq[i]
                if len(ret) >= k:
                    return ret
            else:
                continue
        return ret[:k]