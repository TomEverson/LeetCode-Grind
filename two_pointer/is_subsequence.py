class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        l = len(s) - 1
        r = len(t) - 1

        while r >= 0:
            if t[r] == s[l]:
                l -= 1
            r -= 1

        return l < 0


if __name__ == "__main__":

    s = Solution()

    print(s.isSubsequence(s="axc", t="ahbgdc"))
