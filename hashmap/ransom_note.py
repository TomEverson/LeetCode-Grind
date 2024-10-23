class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        for letter in magazine:
            hashmap[letter] = hashmap.get(letter, 0) + 1

        for letter in ransomNote:
            if letter not in hashmap:
                return False
            hashmap[letter] = hashmap.get(letter, 0) - 1
            if hashmap.get(letter) == 0:
                del hashmap[letter]

        return True


if __name__ == "__main__":
    solution = Solution()

    res = solution.canConstruct(ransomNote="aab", magazine="baa")

    print(res)
