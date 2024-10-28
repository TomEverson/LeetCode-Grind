class Solution:
    def reverseWords(self, s: str) -> str:
        l = len(s) - 1
        res = ""

        while l >= 0:

            while l >= 0 and s[l] == " ":
                l -= 1

            r = l

            while l >= 0 and s[l] != " ":
                l -= 1

            if r >= 0:
                res += s[l+1:r+1] + " "

        return res.strip()


if __name__ == "__main__":
    s = "a good   example"

    sol = Solution()
    print(sol.reverseWords(s))
