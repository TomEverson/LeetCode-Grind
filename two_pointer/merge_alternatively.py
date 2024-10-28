class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0
        r = 0

        res = ""

        while l < len(word1):
            res += word1[l]

            if r < len(word2) and word2[r]:
                res += word2[r]

            l += 1
            r += 1

        if r < len(word2):
            res += word2[r:]

        return res


if __name__ == "__main__":
    word1 = "abcd"
    word2 = "pq"

    s = Solution()

    print(s.mergeAlternately(word1, word2))
