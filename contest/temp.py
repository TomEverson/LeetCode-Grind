class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        l = list(s)

        for _ in range(t):
            i = 0
            while i < len(l):
                if l[i] == "z":
                    l[i: i+1] = "ab"
                    i += 1

                else:
                    l[i] = chr(ord(l[i]) + 1)

                i += 1

        return len(l)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthAfterTransformations(s="abcyy", t=2))
