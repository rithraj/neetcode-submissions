class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        have = defaultdict(int)
        
        for c in s1:
            need[c] += 1

        l = 0

        for r, char in enumerate(s2):
            have[char] += 1

            if r - l + 1 > len(s1):
                have[s2[l]] -= 1
                if have[s2[l]] == 0:          # tidy up so dict equality works
                    del have[s2[l]]

                l += 1
            
            if r - l + 1 == len(s1) and have == need:
                return True

        return False

        
        