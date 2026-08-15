class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # charSet = set(s)
        # res = 0

        # for c in charset:
        #     count = 0
        #     l = 0
        #     for r in range(len(s)):
        #         if s[r] == c:
        #             count += 1

        #         while (r - l + 1) - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l+= 1
                
        #         res = max(res, r - l + 1)

        # return res

        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            currMax = max(count, key=count.get)
            while (r - l + 1) - count[currMax] > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
                currMax = max(count, key=count.get)
            res = max(res, r-l + 1)
        return res
            










