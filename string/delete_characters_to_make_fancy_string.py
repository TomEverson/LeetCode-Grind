class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        count = 1
        current = s[0]

        for r in range(1, len(s)):
            if s[r] == current and count != 2:
                count += 1
                res += s[r]
            elif s[r] != current:
                current = s[r]
                count = 1
                res += s[r]

        return res


if __name__ == "__main__":
    s = Solution()

    print(s.makeFancyString("aaabbb"))
    print(s.makeFancyString("leeetcode"))
