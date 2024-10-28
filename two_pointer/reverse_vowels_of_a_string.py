class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s.strip(""))
        vowel_set = {"a", "e", "i", "o", "u"}
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].lower() in vowel_set and s[r].lower() in vowel_set:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[r].lower() in vowel_set:
                l += 1
            else:
                r -= 1

        return ''.join(s)


if __name__ == "__main__":
    string = "IceCreAm"

    s = Solution()
    print(s.reverseVowels(string))
