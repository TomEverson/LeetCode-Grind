class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        char_to_word: dict[str, str] = {}

        word_to_char: dict[str, str] = {}

        words: list[str] = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            current_char: str = pattern[i]
            word: str = words[i]

            if current_char not in char_to_word and word not in word_to_char:
                char_to_word[current_char] = word
                word_to_char[word] = current_char
            else:
                if char_to_word.get(current_char) != word or word_to_char.get(word) != current_char:
                    return False

        return True


if __name__ == "__main__":
    pattern = "abba"
    s = "dog dog dog dog"

    sol = Solution()
    print(sol.wordPattern(pattern, s))
