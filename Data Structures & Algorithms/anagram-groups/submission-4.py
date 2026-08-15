class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for w in strs:
            charmap = [0] * 26
            for c in w:
                charmap[ord(c) - ord('a')] += 1
            res[tuple(charmap)].append(w)
        
        return list(res.values())