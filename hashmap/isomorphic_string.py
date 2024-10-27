class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashmap = {}

        for index, letter in enumerate(s):
            if letter in hashmap:
                if hashmap[letter] != s[idx]:
                    return False
            hashmap[letter] = t[index]

        for idx, letter in enumerate(t):
            if letter in hashmap:
                if hashmap[letter] != s[idx]:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic(s="badc", t="baba"))
