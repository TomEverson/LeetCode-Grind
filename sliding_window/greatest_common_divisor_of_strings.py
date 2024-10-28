from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2 != str2+str1:
            return ""

        div = gcd(len(str1), len(str2))
        return str1[:div]


if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"

    s = Solution()

    print(s.gcdOfStrings(str1, str2))
