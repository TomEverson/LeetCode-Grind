class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        index = 0
        res = -1

        while (index + len(needle)) <= len(haystack):
            val = haystack[index: index + len(needle)]

            if val == needle:
                res = index
                break

            index += 1

        return res


if __name__ == "__main__":
    haystack = "leetcode"
    needle = "leeto"

    solution = Solution()
    print(solution.strStr(haystack, needle))
