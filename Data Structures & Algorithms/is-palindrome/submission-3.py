class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s = new_s + c
        new_s = new_s.lower()

        if len(new_s) % 2 == 0:
            l,r = len(new_s) // 2 - 1, len(new_s) // 2
        else:
            rem = len(new_s) // 2
            l = rem
            r = rem

        while l >= 0 and r < len(new_s):
            if new_s[l] == new_s[r]:
                print(new_s[l] + " and " + new_s[r])

                l -= 1
                r += 1
            elif new_s[l] != new_s[r]:
                print(new_s[l] + " and " + new_s[r])
                return False
            
        return True
        