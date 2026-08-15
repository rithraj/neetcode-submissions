class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        # I am going to create the keys for the mapping by sorting 
        # the string characters
        for s in strs:
            sorted_chars = ''.join(sorted(s))

            if sorted_chars in anagram_map:
                anagram_map[sorted_chars].append(s)
            else:
                anagram_map[sorted_chars] = [s]
        
        return list(anagram_map.values())
